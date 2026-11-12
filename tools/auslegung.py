#!/usr/bin/env python3
"""AUTARQ-Auslegungsrechner.

Berechnet aus Wohnfläche, Personenzahl, Klimazone und Baustandard:
Heiz-/Kühllast, Warmwasserbedarf, Wärmepumpen-Größe, PV- und Batterie-
Auslegung, Pufferspeicher, Server-Abwärmebeitrag und Investitionskosten.

Nur Python-Standardbibliothek.
"""

from __future__ import annotations

import argparse
import dataclasses
import sys

# ---------------------------------------------------------------------------
# Klimazonen
# ---------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class Klima:
    name: str
    heiztage: int                    # Tage/Jahr mit Heizbedarf
    gradtage: int                    # Gradtagzahl (Basis 15 °C, grob)
    kuehl_faktor: float              # W/m² Kühlbedarf (Spitzenlast)
    pv_ertrag: float                 # kWh pro kWp und Jahr
    kuehl_saison: int                # Tage/Jahr mit Kühlbedarf
    heiz_wasser_c: int               # typ. Vorlauftemperatur


KLIMATA = {
    "kalt":       Klima("Kalt (Nord-/Osteuropa, Gebirge)", 260, 4500, 15.0, 950, 10, 45),
    "gemaessigt": Klima("Gemäßigt (Mitteleuropa)",         210, 3200, 30.0, 1050, 40, 35),
    "warm":       Klima("Warm (Südeuropa, MENA, Tropen)",   40,  600, 70.0, 1600, 200, 18),
}

# Spezifische Heizlast in W/m² nach Baustandard (bei Norm-Außentemperatur)
HEIZLAST_W_M2 = {
    "bestand":   100.0,   # unsaniert
    "saniert":    60.0,
    "neubau":     45.0,
    "passivhaus": 15.0,
}

# COP der kompakten Wärmepumpe (Luft/Wasser, R290, auf Fußbodenheizung)
COP_HEIZEN = 4.0
SEER_KUEHLEN = 5.0

# Warmwasserbedarf pro Person (kWh/Tag, 60 °C-Äquivalent)
WW_KWH_PRO_PERSON = 1.6

# Haushaltsstrombedarf ohne WP/Server (kWh/Jahr, Basis 2 Personen)
HAUSHALT_KWH_BASIS = 1800.0
HAUSHALT_KWH_PRO_PERSON = 600.0

# Investitionskosten (€): (DIY, Serie)
KOSTEN = {
    "pv_pro_kwp":              (400.0, 1000.0),
    "batterie_pro_kwh":        (180.0, 350.0),
    "waermepumpe":             (5000.0, 4000.0),
    "puffer_pro_l":            (1.0, 1.6),
    "server_ems":              (700.0, 2000.0),
    "smart_home":              (500.0, 2000.0),
    "installation_hydraulik":  (800.0, 4000.0),
}


def pufferspeicher_liter(heizlast_kw: float, klima: Klima) -> float:
    faktor = 100.0 if klima.name.startswith("Kalt") else 60.0
    return max(300.0, round(heizlast_kw * faktor / 50.0) * 50.0)


def berechne(args) -> dict:
    klima = KLIMATA[args.klima]
    heizlast_kw = args.flaeche * HEIZLAST_W_M2[args.standard] / 1000.0
    kuehllast_kw = args.flaeche * klima.kuehl_faktor / 1000.0

    ww_kw_jahr = args.personen * WW_KWH_PRO_PERSON * 365.0
    # Heizenergie approximiert über Gradtage relativ zum Referenzfall Mitteleuropa
    heiz_kw_jahr = heizlast_kw * (klima.gradtage / 3200.0) * 2100.0
    # KWL-Wärmerückgewinnung spart ~8 % Heizwärme (kein Fensterlüftungsverlust)
    if args.kwl == "ja":
        heiz_kw_jahr *= 0.92
    # Strahlungswärme (Folie/Farbe/IR): 2–3 K niedrigere Lufttemperatur + Zonensteuerung
    if args.folie_m2 > 0 or args.farbe_m2 > 0:
        heiz_kw_jahr *= 0.85
    kuehl_kw_jahr = kuehllast_kw * klima.kuehl_saison * 8.0

    # Solar-Luftkollektor: 250 kWh/m²/Jahr Wärme (heizsaisonbezogen), begrenzt
    # durch den Heizwärmebedarf; Kühlschränke/TK: 170 kWh/Jahr pro Haushalt
    luftkollektor_kw_jahr = min(heiz_kw_jahr, args.luftkollektor_m2 * 250.0)
    kuehlgeraete_kw_jahr = 0.0 if args.kuehl_abwaerme == "nein" else args.personen * 130.0 * (klima.heiztage / 365.0)

    server_kw_jahr = args.server_w * 8760.0 / 1000.0
    server_nutzbar_heiz = server_kw_jahr * (klima.heiztage / 365.0)

    # COP abhängig vom Temperaturhub: COP = min(12, eta * T_verflüssigung / Hub)
    # eta ~0.45 (guter Inverter-Verdichter), T_verflüssigung 35 °C; praktische
    # Obergrenze 12 (Verdichter-/Pumpenverluste dominieren bei tiny Hub)
    hub = args.hub_k if args.hub_k else 35.0
    cop_heizen = round(min(12.0, 0.45 * (273.15 + 35.0) / max(hub, 1.0)), 1)
    cop_kuehlen = round(min(15.0, 0.45 * (273.15 + 15.0) / max(hub, 1.0)), 1)

    # Folie/Farbe deckt direkt einen Teil des Heizwärmebedarfs (COP 1, aber
    # gezielt und bevorzugt aus PV-Überschuss): max. 25 % des Restbedarfs
    direkt_m2 = args.folie_m2 + args.farbe_m2
    folie_leistung_kw = direkt_m2 * 0.12
    folie_heat_kw_jahr = min(heiz_kw_jahr * 0.25, folie_leistung_kw * 800.0)
    folie_kw_jahr = folie_heat_kw_jahr

    wp_heiz_kw_jahr = max(0.0, heiz_kw_jahr - server_nutzbar_heiz - folie_heat_kw_jahr
                          - luftkollektor_kw_jahr - kuehlgeraete_kw_jahr) / cop_heizen
    wp_ww_kw_jahr = ww_kw_jahr / cop_heizen
    wp_kuehl_kw_jahr = max(0.0, kuehl_kw_jahr) / cop_kuehlen

    kwl_kw_jahr = 0.0 if args.kwl == "nein" else args.flaeche * 0.35 * 8760.0 / 1000.0

    haushalt_kw_jahr = HAUSHALT_KWH_BASIS + max(0, args.personen - 2) * HAUSHALT_KWH_PRO_PERSON
    bedarf_kw_jahr = haushalt_kw_jahr + server_kw_jahr + wp_heiz_kw_jahr + wp_ww_kw_jahr + wp_kuehl_kw_jahr + folie_kw_jahr + kwl_kw_jahr

    pv_kwp = args.pv_kwp if args.pv_kwp else round(bedarf_kw_jahr / klima.pv_ertrag, 1)
    pv_kw_jahr = pv_kwp * klima.pv_ertrag
    autarkie = min(1.0, pv_kw_jahr / bedarf_kw_jahr)

    batterie_kwh = round((bedarf_kw_jahr / 365.0) * 0.6, 1)
    puffer_l = pufferspeicher_liter(heizlast_kw, klima)

    wp_leistung_kw = max(
        max(0.0, heizlast_kw - args.server_w / 1000.0),
        kuehllast_kw,
        2.0,
    )
    wp_leistung_kw = round(wp_leistung_kw, 1)

    kosten_diy = (
        pv_kwp * KOSTEN["pv_pro_kwp"][0]
        + batterie_kwh * KOSTEN["batterie_pro_kwh"][0]
        + KOSTEN["waermepumpe"][0]
        + puffer_l * KOSTEN["puffer_pro_l"][0]
        + KOSTEN["server_ems"][0]
        + KOSTEN["smart_home"][0]
        + KOSTEN["installation_hydraulik"][0]
        + args.folie_m2 * 20.0 + (350.0 if args.folie_m2 > 0 else 0.0)
        + args.farbe_m2 * 12.0 + (250.0 if args.farbe_m2 > 0 else 0.0)
        + args.luftkollektor_m2 * 60.0
        + (300.0 if args.kuehl_abwaerme == "ja" else 0.0)
        + (1000.0 if args.kwl == "ja" else 0.0)
    )
    kosten_serie = (
        pv_kwp * KOSTEN["pv_pro_kwp"][1]
        + batterie_kwh * KOSTEN["batterie_pro_kwh"][1]
        + KOSTEN["waermepumpe"][1]
        + puffer_l * KOSTEN["puffer_pro_l"][1]
        + KOSTEN["server_ems"][1]
        + KOSTEN["smart_home"][1]
        + KOSTEN["installation_hydraulik"][1]
        + args.folie_m2 * 25.0 + (500.0 if args.folie_m2 > 0 else 0.0)
        + args.farbe_m2 * 35.0 + (400.0 if args.farbe_m2 > 0 else 0.0)
        + args.luftkollektor_m2 * 200.0
        + (400.0 if args.kuehl_abwaerme == "ja" else 0.0)
        + (3500.0 if args.kwl == "ja" else 0.0)
    )

    return dict(
        klima=klima, heizlast_kw=heizlast_kw, kuehllast_kw=kuehllast_kw,
        ww_kw_jahr=ww_kw_jahr, heiz_kw_jahr=heiz_kw_jahr, kuehl_kw_jahr=kuehl_kw_jahr,
        server_kw_jahr=server_kw_jahr, server_nutzbar_heiz=server_nutzbar_heiz,
        folie_leistung_kw=folie_leistung_kw, folie_kw_jahr=folie_kw_jahr,
        luftkollektor_kw_jahr=luftkollektor_kw_jahr,
        kuehlgeraete_kw_jahr=kuehlgeraete_kw_jahr,
        cop_heizen=cop_heizen, cop_kuehlen=cop_kuehlen, hub=hub,
        kwl_kw_jahr=kwl_kw_jahr,
        wp_heiz_kw_jahr=wp_heiz_kw_jahr, wp_ww_kw_jahr=wp_ww_kw_jahr,
        wp_kuehl_kw_jahr=wp_kuehl_kw_jahr, haushalt_kw_jahr=haushalt_kw_jahr,
        bedarf_kw_jahr=bedarf_kw_jahr, pv_kwp=pv_kwp, pv_kw_jahr=pv_kw_jahr,
        autarkie=autarkie, batterie_kwh=batterie_kwh, puffer_l=puffer_l,
        wp_leistung_kw=wp_leistung_kw, kosten_diy=kosten_diy, kosten_serie=kosten_serie,
    )


def main() -> int:
    p = argparse.ArgumentParser(description="AUTARQ-Auslegungsrechner")
    p.add_argument("--flaeche", type=float, required=True, help="Wohnfläche in m²")
    p.add_argument("--personen", type=int, required=True, help="Anzahl Personen")
    p.add_argument("--klima", choices=list(KLIMATA), default="gemaessigt",
                   help="Klimazone (default: gemaessigt)")
    p.add_argument("--standard", choices=list(HEIZLAST_W_M2), default="neubau",
                   help="Baustandard (default: neubau)")
    p.add_argument("--server-w", type=float, default=400.0,
                   help="Dauerleistung des Homelab-Servers in W (default: 400)")
    p.add_argument("--pv-kwp", type=float, default=None,
                   help="PV-Größe in kWp (default: automatisch auf Jahresbedarf)")
    p.add_argument("--folie-m2", type=float, default=0.0,
                   help="Carbon-Heizfolie/IR-Fläche in m² (default: 0)")
    p.add_argument("--farbe-m2", type=float, default=0.0,
                   help="Carbon-Heizfarbe (Wand/Decke) in m² (default: 0)")
    p.add_argument("--luftkollektor-m2", type=float, default=0.0,
                   help="Solar-Luftkollektor-Fläche in m² (default: 0)")
    p.add_argument("--kuehl-abwaerme", choices=["ja", "nein"], default="ja",
                   help="Abwärme von Kühl-/Tiefkühlschränken nutzen (default: ja)")
    p.add_argument("--kwl", choices=["ja", "nein"], default="ja",
                   help="Lüftung mit Wärmerückgewinnung (default: ja)")
    p.add_argument("--hub-k", type=float, default=None,
                   help="Temperaturhub der WP in K (default: 35 = konventionell; "
                        "z. B. 3 für Low-Lift-Betrieb mit warmem Puffer als Quelle)")
    args = p.parse_args()

    r = berechne(args)

    print("=" * 62)
    print("AUTARQ – Auslegung")
    print("=" * 62)
    print(f"Szenario        : {args.flaeche:.0f} m², {args.personen} Personen, "
          f"{args.standard}, Server {args.server_w:.0f} W, "
          f"Folie {args.folie_m2:.0f} m², KWL {args.kwl}")
    print(f"Klimazone       : {r['klima'].name}")
    print()
    print("-- Lasten ---------------------------------------------------")
    print(f"Heizlast (Spitze): {r['heizlast_kw']:6.1f} kW "
          f"({HEIZLAST_W_M2[args.standard]:.0f} W/m²)")
    print(f"Kühllast (Spitze): {r['kuehllast_kw']:6.1f} kW")
    print(f"Heizwärmebedarf  : {r['heiz_kw_jahr']:8.0f} kWh/Jahr")
    print(f"Kältebedarf      : {r['kuehl_kw_jahr']:8.0f} kWh/Jahr")
    print(f"Warmwasser       : {r['ww_kw_jahr']:8.0f} kWh/Jahr")
    print()
    print("-- Server-Abwärme -------------------------------------------")
    print(f"Server-Jahreswärme: {r['server_kw_jahr']:7.0f} kWh/Jahr "
          f"(= {args.server_w:.0f} W Dauerlast)")
    print(f"davon im Heizfall nutzbar: {r['server_nutzbar_heiz']:7.0f} kWh/Jahr")
    print(f"  → deckt {100 * r['server_nutzbar_heiz'] / max(r['heiz_kw_jahr'], 1):5.1f} % des Heizwärmebedarfs")
    print()
    print("-- Wärmepumpe (kompakt, Therme-Format) ----------------------")
    print(f"Nennleistung      : {r['wp_leistung_kw']:5.1f} kW modulierend 1–10 kW")
    print(f"Temperaturhub     : {r['hub']:5.1f} K → COP {r['cop_heizen']} (Heizen) / "
          f"{r['cop_kuehlen']} (Kühlen)")
    print(f"Heizstrombedarf   : {r['wp_heiz_kw_jahr']:8.0f} kWh/Jahr (COP {r['cop_heizen']})")
    print(f"Warmwasser-Strom  : {r['wp_ww_kw_jahr']:8.0f} kWh/Jahr")
    print(f"Kühlstrombedarf   : {r['wp_kuehl_kw_jahr']:8.0f} kWh/Jahr (SEER {r['cop_kuehlen']})")
    print()
    print("-- Hybrid: Folie/IR + Lüftung ---------------------------------")
    print(f"Folie/IR Leistung : {r['folie_leistung_kw']:8.1f} kW "
          f"({args.folie_m2:.0f} m² @ 120 W/m²)")
    print(f"Folie/IR Wärme    : {r['folie_kw_jahr']:8.0f} kWh/Jahr (direkt aus PV)")
    print(f"Luftkollektor     : {r['luftkollektor_kw_jahr']:8.0f} kWh/Jahr "
          f"({args.luftkollektor_m2:.0f} m² @ 250 kWh/m²)")
    print(f"Kühlgeräte-Abwärme: {r['kuehlgeraete_kw_jahr']:8.0f} kWh/Jahr (Kühlschrank/TK)")
    print(f"KWL-Strombedarf   : {r['kwl_kw_jahr']:8.0f} kWh/Jahr (WRG + F9-Filter)")
    print()
    print("-- Energiebilanz --------------------------------------------")
    print(f"Haushaltsstrom   : {r['haushalt_kw_jahr']:8.0f} kWh/Jahr")
    print(f"Gesamtbedarf     : {r['bedarf_kw_jahr']:8.0f} kWh/Jahr")
    print(f"PV-Auslegung     : {r['pv_kwp']:8.1f} kWp → {r['pv_kw_jahr']:8.0f} kWh/Jahr")
    print(f"Autarkiegrad     : {100 * r['autarkie']:5.1f} %")
    print(f"Batteriespeicher : {r['batterie_kwh']:8.1f} kWh")
    print(f"Pufferspeicher   : {r['puffer_l']:8.0f} l")
    print()
    print("-- Investitionskosten (Schätzung) ---------------------------")
    print(f"DIY / Second-Life: {r['kosten_diy']:9.0f} €")
    print(f"Serie / Fachbetrieb: {r['kosten_serie']:7.0f} €")
    print("=" * 62)
    print("Hinweis: Richtwerte für die Vorauslegung, keine Planungsgrundlage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
