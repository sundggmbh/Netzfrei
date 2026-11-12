# AUTARQ – Netzentkoppeltes Heizen, Kühlen und Strom für Wohnungen, Häuser und Büros

**Ziel:** Ein bezahlbares System, das Wohnungen, Häuser und Büros weltweit unabhängig vom
Stromnetz macht – mit eigener Stromerzeugung, Heizen in kalten Ländern, Kühlen in warmen
Ländern, und Abwärmenutzung von Servern, Computern, Kühlschränken und Tiefkühlschränken.

## Kernidee

1. **Abwärme ist Wärme.** Ein Server, der 400 W Strom verbraucht, gibt 400 W Wärme ab.
   Statt sie an den Raum zu verlieren, fließt sie in den Pufferspeicher – der Server heizt mit.
2. **Eine kompakte Wärmepumpe als Herzstück.** Maximal so groß wie eine Brennwerttherme
   (ca. 450 × 600 × 300 mm), wandmontierbar oder liegend aufstellbar. Heizen *und* Kühlen.
   Mit **R290 (Propan)** und minimalem Temperaturhub (1–3 K über warmen Puffer +
   große Strahlungsflächen) erreicht sie **COP 8–15** statt üblicher 3–4.
   **Oder noch billiger:** Ein 300–800-€-Split-Klimagerät ist technisch dieselbe
   Wärmepumpe – Umbau-Pfade zu Warmwasser, Wasser, Abluft und PV-Direkt: `11-…`.
3. **Netzfrei – das lokale KI-Heimnetzwerk.** Eine Instanz pro Gebäude, ohne Cloud:
   sie entscheidet, wann Strom verbraucht, gespeichert, verkauft oder verschoben wird –
   abhängig von PV-Ertrag, dynamischen Strompreisen (nachts oft günstig, abends teuer),
   Außentemperatur und dem Verhalten der Bewohner.
4. **Ein Haus, ein Netzwerk.** Licht, Steckdosen, Fußbodenheizung, Kühlung, Serverlast,
   Batterie und Wärmepumpe hängen an **Netzfrei**, dem smarten KI-Netzwerk des Hauses.
5. **Hybrid statt teurer Geräte.** Carbon-Heizfolie und -Heizfarbe (8–20 €/m² bzw.
   10–15 €/m², einfach streichen/verlegen) liefern gezielte Strahlungswärme direkt
   vom PV-Überschuss; die Lüftungsanlage mit F9-Filter liefert pollenfreie Frischluft
   und entfeuchtet – für Allergiker geeignet.
6. **Gratis-Wärme überall abschöpfen.** Sonnen-Luftkollektoren aus schwarzem
   Lochblech (DIY 30–100 €/m², nur ein 5–20-W-Ventilator, bis 40 K Luft-
   temperaturanstieg), Abwärme von Kühl-/Tiefkühlschränken und die Abluft der
   Lüftung als WP-Quelle: zusammen fast der gesamte Heizwärmebedarf eines Neubaus.

## Projektstruktur

```
autarq/
├── README.md                  ← dieses Dokument
├── docs/
│   ├── 01-konzept.md          ← Systemarchitektur, Energieflüsse, Klimazonen
│   ├── 02-waermepumpe.md      ← Speifikation der kompakten Wärmepumpe
│   ├── 03-smart-home-ki.md    ← **Netzfrei**: lokale KI, EMS, Preisoptimierung
│   ├── 04-kosten-roadmap.md   ← Investitionskosten, Umsetzungsphasen
│   ├── 05-hybrid-strahlung.md ← Carbon-Heizfolie, Infrarot, gezieltes Kühlen
│   ├── 06-frischluft-allergiker.md ← KWL, F9/HEPA-Filter, Entfeuchtung
│   ├── 07-heizfarben.md       ← Heizen durch Streichen (Carbon-Heizfarbe)
│   ├── 08-waermequellen.md    ← Solar-Luftkollektoren, Kühlgeräte-Abwärme, Abluft
│   ├── 09-kaeltemittel-niedertemperaturhub.md ← R290 & 1–3 K-Hub-Betrieb (COP 8–15)
│   ├── 10-smart-home-systeme.md ← Systemvergleich & Einkaufsliste für Netzfrei
│   └── 11-klimageraete-umbau.md ← Klimageräte als günstige WP: 5 Umbau-Pfade, Pakete
│   └── 12-sonnenluftkollektor.md ← Wärme aus schwarzem Lochblech (30–100 €/m²)
└── tools/
    └── auslegung.py           ← Auslegungsrechner (Bedarf → Komponenten → Kosten)
```

## Auslegungsrechner

```bash
# Beispiel: Neubau, 120 m², 4 Personen, gemäßigtes Klima (Mitteleuropa),
# Homelab mit 400 W Abwärme
python3 tools/auslegung.py --flaeche 120 --personen 4 --klima gemaessigt \
    --standard neubau --server-w 400

# Warmes Klima (Kühlen im Fokus)
python3 tools/auslegung.py --flaeche 100 --personen 3 --klima warm \
    --standard neubau --server-w 300

# Kaltes Klima (Heizen im Fokus)
python3 tools/auslegung.py --flaeche 140 --personen 4 --klima kalt \
    --standard saniert --server-w 600
```

Alle Parameter: `python3 tools/auslegung.py --help`

## Status

- [x] Systemarchitektur & Konzept
- [x] Auslegungsrechner v1
- [ ] Wärmepumpen-Prototyp-Spezifikation (Details, BOM)
- [ ] EMS-Software (Home-Assistant-basiert, mit lokalem LLM)
- [ ] Pilotinstallation

## Lizenz

Offen geplant (Vorschlag: CERN-OHL-S-2.0 für Hardware, Apache-2.0 für Software) –
Ziel ist, dass sich jeder das System leisten und bauen kann.
