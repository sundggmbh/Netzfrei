# 02 – Kompakte Wärmepumpe (Herzstück)

## 1. Designanforderungen

| Anforderung | Zielwert |
|---|---|
| Abmessungen | max. 450 × 600 × 300 mm (B × H × T) – **kleiner als eine Brennwertgastherme** |
| Montage | Wandmontage **oder** liegend auf dem Boden (beides möglich, wie bei einer Therme) |
| Heizleistung | 1–10 kW modulierend (Inverter-Verdichter, Regelbereich ≥ 1:10) |
| Kühlleistung | gleiches Gerät, reversibel, SEER ≥ 5 |
| Kältemittel | R290 (Propan) – natürlich, kein F-Gas, Füllmenge ≤ 500 g (Kältemittel-Vergleich: `09-kaeltemittel-niedertemperaturhub.md`) |
| Vorlauftemperatur | bis 55 °C (kompatibel mit Fußbodenheizung *und* Radiatoren im Bestand) |
| Warmwasser | integrierter Durchlauf- oder kleiner intern. Speicher (80–120 l) |
| Anbindung | Wasser-Hydraulik (Vor/Rück), 230-V-Netz, Bus (Modbus/Ethernet) ans EMS |
| Geräusch | ≤ 35 dB(A) in 1 m (für Wohnräume tauglich) |
| Zielkosten | ≤ 4.000 € in Serie |

## 2. Architekturvarianten

### Variante A – Luft/Wasser-Monoblock (empfohlen für den Start)
- Komplette Kältetechnik (Verdichter, Lamellenwärmetauscher mit leisem Axialventilator,
  Expansionsventil, Plattenwärmetauscher) in einem Gehäuse.
- **Problem:** braucht Luftanschluss. Lösung: Aufstellung an einer Außenwand mit
  Wanddurchführung (2 Ø-160-mm-Rohre) oder auf dem Flachdach/Balkon – das Innengerät
  bleibt thermenklein, die Lufteinheit ist flach (≤ 120 mm Tiefe).
- Vorteil: einfache Technik, bewährte Komponenten, selbst baubar aus
  Serienteilen (z. B. modulierende Inverter-Rotationsverdichter aus Klimasplitgeräten).

### Variante B – Wasser/Wasser mit Erdsonde oder Brunnen
- Höchste Effizienz (COP 5+), komplett lautlos im Gebäude.
- Höhere Installationskosten (Bohrung/Sonde) – für Neubauten mit Erdreichanschluss
  als Upgrade-Option vorgesehen.

### Variante C – Abwärme-/Kollektor-gekoppelt (Brine/Wasser)
- Verdampferseitig an einen Solarkollektor-/Luftabsorber-Kreis gekoppelt: Die WP nutzt
  Kollektorwärme als Wärmequelle → COP steigt im Winter auf 4,5–5,5.
- Kombinierbar mit Variante A als Hybrid (Luft bei Bedarf, Kollektor wenn Sonne).

## 3. Minimaler Temperaturhub (1–3 K) als Designziel

Der größte Effizienzhebel ist nicht das Kältemittel, sondern der **Temperaturhub**:
Jede 1 K weniger Hub = 2–4 % mehr COP. Gemessen: COP 11,4 bei 13 K Hub (vs. ~4
bei 40 K). Unser System hält Quelle und Senke warm und nah beieinander:

- **Quelle:** Pufferspeicher 19–22 °C, geladen von Server-Abwärme,
  Luftkollektor, KWL-Abluft, Erdreich – statt kalter Außenluft.
- **Senke:** Fußboden/Kühldecke 22–26 °C über große Strahlungsflächen –
  statt 40 °C Vorlauf.
- **Ergebnis:** Hub 2–3 K an den meisten Tagen → **COP 8–15**.

Technik dafür: überfluteter Verdampfer (+16–48 %), übergroße Platten-
wärmetauscher (Nähe ≤ 1–2 K), Ejektor statt Drossel. Details und
Jahresverlauf-Tabelle: `09-kaeltemittel-niedertemperaturhub.md`.

## 4. Betriebsmodi (reversibel)

| Modus | Pufferspeicher | Fußbodenkreis | Quelle |
|---|---|---|---|
| **Heizen** | 35–50 °C | Vorlauf 30–35 °C | Außenluft / Kollektor / Server-Abwärme |
| **Kühlen** | 9–18 °C | Vorlauf 15–18 °C (Tauwacht) | Außenluft (Nachtauskühlung) / Erdreich |
| **Warmwasser** | Priorität, Legionellenschaltung | – | wie Heizen |
| **Free Cooling** | – | direkt aus Puffer/Erde | ohne Verdichter, nur Pumpe |
| **Server-Kühlung** | Kühlkreis-Anschluss | – | Homelab wassergekühlt |

## 5. Regelung durch das EMS

Die Wärmepumpe ist kein eigenständiges Gerät, sondern ein **Aktor des Energieleitsystems**:

- EMS sagt Leistungsvorgabe (kW), Modus (heizen/kühlen/WW) und Zeitfenster vor.
- Die KI startet den Verdichter bevorzugt, wenn PV-Überschuss oder billiger Netzstrom
  verfügbar ist (siehe `03-smart-home-ki.md`) und lädt den Pufferspeicher thermisch auf.
- Der Pufferspeicher ist damit auch ein **Stromspeicher-Ersatz**: 500 l Wasser mit
  ΔT = 30 K speichern ~17 kWh Wärme – deutlich billiger pro kWh als eine Batterie.

## 6. Selbstbau-/Seriendreiteile (Kostenweg)

Komponenten, die es heute am Markt günstig gibt und die den Prototyp bilden können:

- Modulierender Inverter-Rotationsverdichter (R290) aus Klimasplit-Industrieteilen
- Plattenwärmetauscher (Brazed-Plate, 316L) – Standardteil, 80–150 €
- EC-Axialventilator (leise, 190–240 mm)
- Elektronisches Expansionsventil + Controller
- Pumpe (Grundfos ALPHA2-Klasse) für den Wasserseitenkreis
- Gehäuse: Blech oder 3D-gedruckte/gefräste Variante im Therme-Format

Damit ist eine Serienstückzahl von 100–1.000 Stück zu ≤ 4.000 € realistisch;
Einzelbauaktuell eher 5.000–7.000 €.
