# 05 – Hybrid-System: Strahlungswärme, direkte Kühlung, gezielter Komfort

## 1. Grundprinzip: Wärme dahin, wo der Mensch ist

Konventionelle Heizungen erwärmen die ganze Luft im Raum – teuer und träge.
Strahlungswärme (Infrarot, Carbonfolien) erwärmt **direkt Menschen, Oberflächen
und Gegenstände**. Folge:

- **Gleiche Behaglichkeit bei 2–3 K niedrigerer Lufttemperatur** → 10–15 %
  weniger Heizenergie.
- **Sekundenschnelle Reaktion** – ideal für die KI-Steuerung: Räume werden nur
  geheizt, wenn und wo jemand da ist.
- **Keine teuren Geräte**: Heizfolie ist ein Passivprodukt, kein Kompressor,
  kein Wartungsfall.

## 2. Komponenten (alle kostengünstig)

| Komponente | Technologie | Kosten | Einsatz |
|---|---|---|---|
| **Carbon-Heizfolie** | 12–24 V/230 V, 100–150 W/m², unter Bodenbelag, Wand oder Decke | **8–20 €/m²** (Folienware) | Grund-/Zonenheizung im Neubau, unter Laminat, Fliesen, Teppich |
| **Infrarot-Paneele** | 60–800 W, Bild-/Spiegel-/Deckenpaneel | 60–200 €/Stück | Nachrüstung, Punktbeheizung (Bad, Arbeitsplatz) |
| **Carbonfolie zum Auflegen** | selbstklebend, 12 V Niedervolt | 10–25 €/m² | Möbelintegriert, Sitzflächen, Fußbodenmatten |
| **Kühldecke (passiv)** | Kühlkreis an Decke/Wand | hydraulisch vorhanden | Sommer: Decke 17–19 °C strahlt Kälte ab |

**Warum das so billig ist:** Heizfolie ist Industrieware aus der
Verpackungs-/Automobilbranche (Sitzheizungen). Keine Spezialfirmen nötig –
Verlegen wie eine Dampfsperre unter dem Bodenbelag.

## 3. Die Hybrid-Logik (KI-gesteuert)

Das System kombiniert drei Hebeleben nach Kosten-Nutzen:

```
1. SERVER-ABWÄRME + SOLARKOLLEKTOR  → kostenlos, Grundlast im Pufferspeicher
2. WÄRMEPUMPE (COP 4–5)             → Fußbodenheizung 30–35 °C, Grundtemperatur
3. CARBONFOLIE / IR (COP 1, aber:)  → gezielt, schnell, nur wo Menschen sind,
   direkt aus PV-Überschuss            direkt vom PV-Strom speisbar
```

**Die KI entscheidet pro Raum und Minute:**

- **PV-Überschuss mittags** → Folien laufen direkt vom PV-Strom (kein Umweg
  über Batterie/WP = beste Ausnutzung jedes kWh).
- **Abwesende Räume** → Folie aus, Fußboden auf Frostschutz.
- **Anwesenheit erkannt** → IR-Paneel/Folie im Aufenthaltsbereich vorheizen,
  während die träge Fußbodenheizung nachzieht.
- **Nacht/abwesend** → nur minimale Grundtemperatur; morgens 10 Minuten vor
  Aufstehen Folien-Burst im Bad/Schlafzimmer.
- **Sommer** → dieselbe Steuerung invertiert: Deckenkühlung + gezielte
  Kühlung der Aufenthaltszone, Nachtauskühlung des Pufferspeichers.

**Energie-Ersparnis des Hybrids** gegenüber reiner WP-Fußbodenheizung:

- 10–15 % durch niedrigere Lufttemperatur (Strahlungsanteil)
- 10–20 % durch Zonen-/Anwesenheitssteuerung
- 5–10 % durch direkte PV-Nutzung ohne Speicherverluste
- **Insgesamt ~25–40 % weniger Heizenergie** – bei Folien-Investition von
  nur 1.000–2.500 € für eine 120-m²-Wohnung.

## 4. Gezieltes Kühlen (wie eine Klimaanlage, ohne Zugluft)

- **Kühldecke/-wand** über den Kühlkreis der Wärmepumpe (Vorlauf 15–18 °C,
  Tauwacht durch den EMS): entzieht Wärme **strahlend**, ohne Luft zu bewegen.
- **Gezielte Zonenkühlung:** Nur der Aufenthaltsraum wird gekühlt, nicht das
  ganze Gebäude – gleiche Logik wie beim gezielten Heizen.
- **Entfeuchtung:** Die WP erzeugt im Kühlbetrieb 9–12 °C kaltes Wasser; ein
  kleiner Umluft-Konvektor (oder die Lüftungsanlage, siehe `06-frischluft-allergiker.md`)
  führt Luft über den Kühler unter Taupunkt → Kondensat ab. Entfeuchtung ist
  damit ein Nebenprodukt – **kein extra Entfeuchter nötig**.

## 5. Kostenauswirkung (120 m² Neubau, 4 Personen)

| Posten | Kosten |
|---|---|
| Carbon-Heizfolie 80 m² aktiv verlegt | 1.200–1.600 € |
| IR-Paneele 3 Stück (Bad, Flur, Arbeitsplatz) | 300–500 € |
| Thermostate/Zonenaktoren (8 Zonen) | 200–400 € |
| **Summe Zusatzinvest** | **~1.700–2.500 €** |
| Einsparung Heizenergie (25–35 % von ~11.300 kWh) | ~3.000–4.000 kWh/Jahr |
| Ersparnis WP-Strom (bei COP 4) | ~750–1.000 kWh/Jahr ≈ 200–300 €/Jahr |
| **Amortisation** | **6–10 Jahre** – oder sofort, wenn PV-Überschuss sonst ungenutzt ins Netz geht |

## Ergänzung: Induktion als Hebebene 3b

Neben Folie/Farbe (COP 1,0) gibt es **Induktion** (Wirbelströme, ~25–60 kHz,
COP ~0,85): keine Grundheizung, aber einzigartige Nischen – kontaktlose
Tank-Erwärmung ohne Heizstab, induktive WP-Abtauung, Frostschutz, Boost.
Details und Realitätscheck: `15-induktionswaerme.md`.
