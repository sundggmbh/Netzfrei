# 11 – Klimageräte-Umbau: Die günstige Wärmepumpe

## 1. Der Preis-Wahrheits-Satz

**Ein reversibles Split-Klimagerät IST eine Wärmepumpe** – gleiche Komponenten
(Verdichter, 4-Wege-Umschaltventil, Wärmetauscher), gleiche Physik:

| | Split-Klimagerät | „Wärmepumpe" (Luft/Wasser) |
|---|---|---|
| Preis (Gerät) | **300–800 €** (Einzel-Split) | 6.000–15.000 € |
| Preis (installiert) | 1.500–8.500 € (Multi-Split) | 13.000–30.000 € (Buderus-Angabe) |
| COP/SCOP | 3,0–4,5 / **4–5** (SCOP, Bosch-Angabe) | 3,5–4,5 / 4–5 |
| Heizbereich | bis −15 °C Standard, −25 °C „Hyper Heating" | bis −20 °C |
| Kühlen | serienmäßig | nur mit reversibler Ausführung |
| Heißes Gas (Verdichterabgang) | **vorhanden** (60–80 °C) | vorhanden |

**Der Unterschied ist der Preis, nicht die Technik.** Die Klimageräte-Industrie
produziert Jahrzehnte der Massenfertigung – deshalb der Preis. (Ehrliche
Einschränkung: klimaaktiv rät davon ab, ein Klimagerät *nur* zum Heizen zu
kaufen – es lohnt sich durch die Ganzjahresnutzung: Kühlen + Heizen + Warmwasser.)

## 2. Fünf Umbau-Pfade (aufsteigender Aufwand)

### Pfad A –Direkt heizen/kühlen (kein Umbau)
Split-Gerät als Luft-Luft-WP: Sommer kühlen, Winter heizen, minutes-schnell.
Kopplung an Heizfolie/Farbe (siehe `05-…`): Die Folie übernimmt die
Grundtemperatur, das Split-Gerät die Spitzen. **Kosten: Gerät allein.**

### Pfad B – Brauchwasser-Warmwasser (belegter DIY-Weg)
**Desuperheater/Heat-Recovery-Einheit** am heißen Verdichter-Abgang
(z. B. HotSpot HRU, **400–500 €**): Das heiße Gas (60–80 °C) vor dem
Kondensator erwärmt Brauchwasser – im Kühlbetrieb **gratis Warmwasser**
(die Wärme muss ohnehin abgeführt werden), im Heizbetrieb mit leichtem
Effizienzverlust am Kondensator. Belegt: Supermärkte decken so ihren
gesamten Warmwasserbedarf aus Kälteanlagen.
**Vorsicht:** Nur in Kupferleitungen eingreifen (Aluminium nicht lötbar);
Wassertemperatur-Begrenzung (Legionellen-/Verbrühungsschutz).

### Pfad C – Luft→Wasser-Umbau (DIY dokumentiert)
Außengerät des Splits entkoppeln, **Plattenwärmetauscher** zwischen
Verdichter und Kondensator, Wasserseite auf 120-l-Doppelspiral-Speicher
(belegt: harizanov-Daikin-Hack; DIY-Solarforum: Mini-Split 12.000 BTU →
Fußbodenheizung mit sehr hoher Effizienz wegen niedrigem Hub).
Ergebnis: eine Luft-Wasser-WP für **~600–1.200 €** (Gerät + Platten-WT +
Pumpen + Regelung) statt 13.000 €.
**Kältemittel-Arbeit nur durch Kältetechniker** (R32/R290, Anlage öffnen =
Sachkunde nach CHEM-RECHT/EU 517/2014 nötig).

### Pfad D – Abluft-Kopplung (COP-Boost)
Außengerät nicht an Außenluft, sondern in eine **Abluft-Box** hinter der
KWL (Rest-Abluft 5–8 °C statt −10 °C Außenluft): COP steigt von ~3 auf
4–5 im Winter. Gleicher Trick wie in `08-waermequellen.md` – aber ohne
eigene WP, mit dem 300-€-Klimagerät.

### Pfad E – PV-Direktbetrieb (netzfrei im Sommer)
**Solar-Klimageräte** (z. B. HotSpot ACDC12C-Klasse) laufen **direkt von
PV-Modulen** (DC-Einspeisung, kein Wechselrichter, kein Netz nötig tagsüber).
Für Büros/Wohnungen in sonnenreichen Ländern die billigste Klima-Wärme der Welt.

## 3. Das Baukastensystem (je nach Nutzung)

### Paket „Wohnung" (Miete, 50–80 m²)
| Baustein | Kosten |
|---|---|
| Balkonkraftwerk 800 W | 300–500 € |
| Batterie 2–5 kWh (Second-Life) | 400–1.200 € |
| Split-Klimagerät (heizen/kühlen) | 400–700 € |
| Heizfolie/Farbe 20–40 m² | 300–800 € |
| Desuperheater-Warmwasser (Pfad B, optional) | 400–500 € |
| **Summe** | **~1.400–3.700 €** |
→ Heizen, Kühlen, Warmwasser-Vorwärmung, eigener Strom – ohne Eingriff in
Gebäudeinfrastruktur.

### Paket „Büro" (100–300 m², Tageslast)
| Baustein | Kosten |
|---|---|
| Multi-Split 2–4 Innengeräte (PV-Direkt bevorzugt) | 1.500–4.000 € |
| Balkon-/Dach-PV 3–10 kWp | 1.200–10.000 € |
| Batterie 5–15 kWh | 1.000–4.000 € |
| Heizfolie/Farbe Decken/Wand | 800–2.500 € |
| KWL + Luftkollektor (siehe `06-…`, `08-…`) | 1.000–2.100 € |
| Netzfrei-Server (EMS + Homelab) | 700–1.500 € |
| **Summe** | **~6.200–24.100 €** |
→ Büro klimatisiert + beheizt + Warmwasser + Netzfrei-Tagstrom.

### Paket „Haus" (Neubau, 120 m², vollautark)
Wie `04-kosten-roadmap.md` – nur ersetzt der Klimageräte-Wasser-Umbau (Pfad C)
die Prototyp-WP: **WP-Posten sinkt von 4.000–5.000 € auf 600–1.200 €**,
Gesamtsystem ab ~9.000 € DIY.

## 4. Regelung durch Netzfrei

- Split-Geräte sind **nicht nativ Modbus-fähig** → Anbindung über
  IR-Bridge (10 €) oder Klimageräte-WLAN-Adapter mit lokaler API
  (z. B. ESPHome/Midea-Hass-Integrationen – kein Cloud-Zwang).
- Netzfrei entscheidet: Kühlen/Heizen/Sperre, PV-Überschuss → Vollgas-Kühlen
  (Büro vorkühlen), Desuperheater-Priorität für Warmwasser, Folien-Unterstützung
  bei Frost.
- **Grenze:** Keine modulierende Vorlauftemperatur wie bei echter WP –
  die Wasser-Pfade (B/C) lösen das.

## 5. Risiken & Grenzen (ehrlich)

- **R32** ist in den meisten günstigen Geräten (GWP 675) – ab 2027 für neue WP
  verboten; für Klimageräte läuft die Frist später, aber R290-Geräte sind die
  zukunftssichere Wahl (werden bereits angeboten).
- **Kältemittel-Arbeiten** brauchen Sachkunde – alle Pfade B/C sind
  Kältetechniker-Territorium; Pfade A/D/E sind DIY-tauglich.
- **Kein Feldtest-SCOP** für Luft-Luft (Heat Pumps Watch: keine systematischen
  Studien) → Pilotmessung in Phase 4 vorgesehen.
- Im Altbau allein heizen lassen Klimageräte zu oft in den ineffizienten
  Bereich fallen – Kombination mit Folie/Farbe/Abwärme ist der AUTARQ-Ansatz.
