"""Netzfrei-EMS: regelbasierte Energiewirtschaft v1.

Priorisierung (docs/03-smart-home-ki.md):
1. Eigenverbrauch maximieren (PV + Server-Abwaerme zuerst nutzen)
2. Kosten minimieren (Preisfenster)
3. Autarkie (Batterie/Puffer)
4. Komfort (nur wenn 1-3 nicht verletzt)

Motto: Einfach, kostenguenstig, unabhaengig - fuer jeden bezahlbar.
"""

from __future__ import annotations

import dataclasses

KOMFORT_MIN_C = 20.0
KOMFORT_NOTFALL_C = 19.0
KOMFORT_MAX_C = 22.0
PREIS_GUENSTIG_CT = 15.0
PREIS_TEUER_CT = 35.0
PUFFER_SOLL_C = 35.0
PUFFER_MIN_C = 30.0
BATTERIE_ZIEL_SOC = 0.90
BATTERIE_RESERVE_SOC = 0.20
KOLLEKTOR_DELTA_K = 8.0
WP_LEISTUNG_KW = 5.0
FOLIE_LEISTUNG_KW = 1.5
INDUKTION_LEISTUNG_KW = 2.0


@dataclasses.dataclass(frozen=True)
class Zustand:
    stunde: int
    pv_w: float
    verbrauch_w: float
    server_w: float
    batterie_soc: float
    preis_ct: float
    raum_temp_c: float
    puffer_temp_c: float
    kollektor_temp_c: float
    verdampfer_frost: bool = False


@dataclasses.dataclass(frozen=True)
class Entscheidung:
    wp_kw: float
    folie_kw: float
    induktion_kw: float
    kwl_stufe: int
    kollektor_luefter: bool
    batterie: str
    aktion: str
    gruende: tuple


def entscheidung(
    wp_kw: float,
    folie_kw: float = 0.0,
    induktion_kw: float = 0.0,
    kwl_stufe: int = 1,
    kollektor_luefter: bool = False,
    batterie: str = "-",
    aktion: str = "",
    gruende: tuple = (),
) -> Entscheidung:
    return Entscheidung(
        wp_kw=round(wp_kw, 2),
        folie_kw=round(folie_kw, 2),
        induktion_kw=round(induktion_kw, 2),
        kwl_stufe=kwl_stufe,
        kollektor_luefter=kollektor_luefter,
        batterie=batterie,
        aktion=aktion,
        gruende=gruende,
    )


def entscheide(z: Zustand) -> Entscheidung:
    gruende = []
    ueberschuss_w = z.pv_w + z.server_w - z.verbrauch_w

    if z.kollektor_temp_c > z.puffer_temp_c + KOLLEKTOR_DELTA_K:
        gruende.append(
            f"Kollektor {z.kollektor_temp_c:.0f} C > Puffer + {KOLLEKTOR_DELTA_K:.0f} K: Luefter an (gratis Waerme)"
        )
        kollektor = True
    else:
        kollektor = False

    if z.verdampfer_frost:
        gruende.append("Verdampfer vereist: Abtau-Boost (Induktion), Verdichter steht")
        return entscheidung(
            wp_kw=0.0,
            induktion_kw=INDUKTION_LEISTUNG_KW,
            kwl_stufe=1,
            kollektor_luefter=kollektor,
            batterie="-",
            aktion="abtauung",
            gruende=gruende,
        )

    if z.raum_temp_c < KOMFORT_NOTFALL_C:
        gruende.append(f"Komfort-Notfall {z.raum_temp_c:.1f} C < {KOMFORT_NOTFALL_C:.0f} C: sofort Waerme")
        wp_kw = WP_LEISTUNG_KW if z.puffer_temp_c > PUFFER_MIN_C else 0.0
        folie_kw = FOLIE_LEISTUNG_KW if z.puffer_temp_c <= PUFFER_MIN_C else 0.0
        gruende.append(
            "WP aus Puffer" if wp_kw > 0 else "Puffer erschöpft: Folie/Boost direkt"
        )
        return entscheidung(
            wp_kw=wp_kw,
            folie_kw=folie_kw,
            induktion_kw=0.0,
            kwl_stufe=2,
            kollektor_luefter=kollektor,
            batterie="-",
            aktion="komfort_notfall",
            gruende=gruende,
        )

    if ueberschuss_w > 0:
        if z.batterie_soc < BATTERIE_ZIEL_SOC:
            gruende.append(
                f"Ueberschuss {ueberschuss_w:.0f} W (PV+Server): Batterie laden ({z.batterie_soc:.0%} < {BATTERIE_ZIEL_SOC:.0%})"
            )
            batterie = "laden"
            wp_kw = 0.0
            aktion = "ueberschuss_batterie"
            if z.puffer_temp_c < PUFFER_SOLL_C:
                wp_kw = min(WP_LEISTUNG_KW, ueberschuss_w / 1000.0 * 0.5)
                aktion = "ueberschuss_batterie_puffer"
                gruende.append(f"Puffer unter Soll {PUFFER_SOLL_C:.0f} C: WP aus PV-Ueberschuss")
        else:
            gruende.append(
                f"Batterie voll ({z.batterie_soc:.0%}): Ueberschuss in Waerme (Puffer/Folie)"
            )
            batterie = "-"
            wp_kw = min(WP_LEISTUNG_KW, ueberschuss_w / 1000.0 * 0.5) if z.puffer_temp_c < PUFFER_SOLL_C else 0.0
            aktion = "ueberschuss_waerme" if wp_kw > 0 else "ueberschuss_einspeisung"
            if wp_kw == 0.0 and z.raum_temp_c < KOMFORT_MAX_C:
                gruende.append("Rest-Ueberschuss: Folie als Direktwaerme")
                return entscheidung(
                    wp_kw=0.0,
                    folie_kw=FOLIE_LEISTUNG_KW,
                    kwl_stufe=2,
                    kollektor_luefter=kollektor,
                    batterie="-",
                    aktion="ueberschuss_folie",
                    gruende=gruende,
                )
        return entscheidung(
            wp_kw=wp_kw,
            kwl_stufe=2,
            kollektor_luefter=kollektor,
            batterie=batterie,
            aktion=aktion,
            gruende=gruende,
        )

    if z.preis_ct <= PREIS_GUENSTIG_CT and z.puffer_temp_c < PUFFER_SOLL_C:
        gruende.append(
            f"Guenstiges Fenster {z.preis_ct:.0f} ct < {PREIS_GUENSTIG_CT:.0f} ct: Puffer laden"
        )
        return entscheidung(
            wp_kw=WP_LEISTUNG_KW,
            kwl_stufe=1,
            kollektor_luefter=kollektor,
            batterie="laden" if z.batterie_soc < BATTERIE_ZIEL_SOC else "-",
            aktion="preisfenster_puffer",
            gruende=gruende,
        )

    if z.preis_ct >= PREIS_TEUER_CT and z.puffer_temp_c >= PUFFER_MIN_C:
        gruende.append(
            f"Teures Fenster {z.preis_ct:.0f} ct >= {PREIS_TEUER_CT:.0f} ct: WP aus, aus Puffer heizen"
        )
        return entscheidung(
            wp_kw=0.0,
            kwl_stufe=1,
            kollektor_luefter=kollektor,
            batterie="entladen" if z.batterie_soc > BATTERIE_RESERVE_SOC else "-",
            aktion="teuer_puffer",
            gruende=gruende,
        )

    gruende.append("Normalbetrieb: WP moduliert auf Bedarf")
    return entscheidung(
        wp_kw=WP_LEISTUNG_KW * 0.5,
        kwl_stufe=1,
        kollektor_luefter=kollektor,
        batterie="-",
        aktion="normal",
        gruende=gruende,
    )
