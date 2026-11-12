# 12 – Sonnen-Luftkollektor: Wärme aus schwarzem Lochblech

## 1. Das Prinzip: so einfach wird Solarwärme

**Transpirierter Sonnenkollektor** (engl. transpired air collector) – das
einfachste Solarthermie-System, das es gibt:

```
Sonne ──► SCHWARZES LOCHBLECH (Absorber, 0,5–1 mm Alu/Stahl)
              │  Luft strömt durch die Löcher → Wirbelung
              │  → beste Wärmeübertragung (Turbulenz statt Grenzschicht)
              ▼
        HINTERLUFTRAUM (gedämmt, 80–100 mm)
              │
        KLEINER VENTILATOR (5–20 W, PV- oder Netzfrei-betrieben)
              │
              ▼
        WARMluft 40–60 °C → ins Gebäude / in die KWL / in den Puffer
```

**Warum Lochblech statt glatter Platte:** Die Zwangs-Wirbelung durch die
Löcher zerstört die isolierende Grenzschicht an der Platte – die
Wärmeübertragung Luft↔Blech ist nahezu perfekt, der Absorber bleibt selbst
kühl (weniger Strahlungsverluste). Das ist der Trick, der den einfachen
Kollektor so effizient macht.

**Kein Wasser, kein Frostschutz, keine Pumpe, kein Druck, kein Wartungsfall.**
Nur ein Ventilator mit 5–20 W – der Kollektor erzeugt das 20–80-Fache seiner
eigenen Aufnahmeleistung als Wärme.

## 2. Belegte Leistungswerte

| Kennwert | Wert | Quelle |
|---|---|---|
| Temperaturanstieg Luft | **17–28 K** Standard (z. B. 0 °C → 20–28 °C) | Transpired-Collector-Literatur (Construction Specifier) |
| Temperaturanstieg max. | **bis 40 K** (niedriger Volumenstrom, Glasabdeckung, hohe Einstrahlung) | Praxisberichte DIY/Hersteller |
| Wärmeleistung | **200–400 W/m²** an klarem Wintertag | BuildItSolar-Messreihen |
| Jahresertrag | 200–350 kWh/m²/Jahr (Südwand Mitteleuropa) | Solarthermie-Richtwerte |
| Ventilator-Strom | 5–20 W (EC-Radialventilator) | – |
| Erntefaktor (Wärme ÷ Ventilator-Strom) | **20–80** | Eigenberechnung |
| Baukosten DIY | **30–80 €/m²** | BuildItSolar (Dosen-/Sieb-Absorber belegt) |
| Baukosten Lochblech-Variante | 40–100 €/m² (Lochblech + Rahmen + Dämmung + Ventilator) | Materialpreise |
| Fertiggeräte | 150–300 €/m² | Markt (Transpired Collector) |
| Amortisation DIY | **1–3 Jahre** | BuildItSolar |

**Messplan (Phase 4, Pilot):** Temperatur vor/nach Kollektor + Volumenstrom +
Einstrahlung (Pyranometer, ~50 €) → Wärmeleistung und Erntefaktor werden exakt
gemessen und im Repo dokumentiert. Der Nutzer-Ansatz („bis 40 K über 20 °C
Luftzug") ist mit Glasabdeckung und gedrosseltem Volumenstrom reproduzierbar.

## 3. Selbstbau in 4 Stufen (1 m²-Modul, skalierbar)

| Stufe | Material | Kosten |
|---|---|---|
| 1. Rahmen | Holz/Alu-Winkel, 80–100 mm tief, Rückwand gedämmt (50 mm) | 10–20 € |
| 2. Absorber | **Schwarzes Lochblech** (Alu/Stahl, Ø 2–5 mm Löcher, 30–50 % Offenfläche, matt-schwarz beschichtet) | 15–35 €/m² |
| 3. Abdeckung | Twinwall-Polycarbonat (optional, +10–15 K und Wetterschutz) | 10–20 €/m² |
| 4. Ventilator + Röhre | EC-Ventilator 5–20 W, Flexrohr ins Gebäude, Rückschlagklappe | 20–40 € |
| **Summe** | | **~55–115 €/m²** |

**Auslegungsregeln:**
- Südausrichtung (±30°), keine Verschattung 9–15 Uhr
- Volumenstrom: 30–80 m³/h pro m² (niedriger = heißere Luft, hoher = mehr
  Gesamtwärme – Netzfrei regelt das nach Einstrahlung)
- 1 m² Kollektor unterstützt 5–10 m² Wohnfläche
- Anschluss-Priorität (Netzfrei entscheidet): 1. KWL-Zuluft-Vorwärmung →
  2. Pufferspeicher (Luft-Wasser-WT) → 3. Direkt in Raum

## 4. Warum dieses System das AUTARQ-Rückgrat für Wärme ist

- **Billigste Wärmequelle überhaupt:** 30–100 €/m² einmalig, danach 20+ Jahre
  fast kostenlos (nur Ventilator-Strom, der aus PV kommt).
- **Funktioniert bei kurzer Einstrahlung** – ein klarer Wintervormittag genügt;
  diffuse Bewölkung liefert noch 30–50 %.
- **Keine Gefahr, kein Druck, kein Kältemittel** → jeder Selbstbauer, jede
  Gemeinde, jedes Land kann das bauen. Ideal für den weltweiten Anspruch.
- **Skaliert modulweise:** 1-m²-Module zu Wänden (10–30 m² Fassade = 2–10 kW
  Solarwärme an Sonnentagen).
- **Doppelnutzung im Sommer:** Nachts verkehrt betrieben = Nachtauschkühler
  (Blech strahlt in den Himmel, Luft kühlt das Gebäude).

## 6. Server-Ventilatoren & Server-Abluft integrieren

### 6.1 Server-Lüfter als Kollektor-Antrieb (gratis Hochtechnologie)

Ausrangierte Server liefern **Hot-Swap-EC-Ventilatoren** (40/60/80 mm,
12 V, PWM-geregelt, 50.000+ h Lebensdauer) – normalerweise Schrott, für den
Kollektor erstklassige Antriebe:

| Vorteil | Auswirkung |
|---|---|
| **12 V DC, PWM-steuerbar** | Direkt am PV-Modul (12-V-Panel + Ladecontroller oder direkt mit Überspannungsschutz) – kein Wechselrichter, kein Netz, kein Netzteil nötig |
| **Stufenlos regelbar (PWM)** | Netzfrei steuert den Volumenstrom nach Einstrahlung – genau die Regelung, die der Kollektor braucht |
| **Kaskadierbar** | 2–6 Lüfter parallel = Redundanz (ein Ausfall fällt nicht auf) und mehr Druck für Lochblech-Gegendruck |
| **Kosten** | ~0 € aus ausrangierten Servern (Ersatzteilmarkt sonst 5–15 €/Stück) |

**Einbau:** Lüfterwand am Kollektor-Austritt (Druckseite), Rückseite mit
Staubschutz (G4-Vorfilter-Material), Sommer-/Winterklappe. Der Homelab-
Server liefert die Lüfter gleich mit – er ist ohnehin Teil des Systems.

### 6.2 Server-Abluft als Wärmequelle im Kollektor-Kreis

Die Server-Abluft (35–45 °C) ist **wärmer als alles, was der Kollektor allein
aus Sonnenlicht macht** (40–60 °C Spitze). Beide kombinieren:

```
Winter (Heizbetrieb):
  KWL-Frischluft (−5 °C)
    → SONNEN-LUFTKOLLEKTOR (+20 bis +40 K → 15–35 °C)
    → SERVER-RAUM (nimmt Server-Abwärme auf → 35–45 °C)
    → Pufferspeicher / Räume (Luft-Wasser-WT)

  → Jede kWh Strom im Server wird zweimal genutzt:
    1. als Rechenleistung
    2. als Wärme im Luftkreis – plus Sonnen-Boost obendrauf

Sommer (Kühlbetrieb):
  Server-Abluft (35–45 °C)
    → KOLLEKTOR (nachts verkehrt: Strahlungskühlung ans Himmelszelt,
      tagsüber als Schornstein nach außen)
    → Server-Raum bleibt kühl OHNE Zusatzstrom
```

**Luftweg-Regelung durch Netzfrei:** Ventile/Klappen schalten je nach
Saison und Einstrahlung zwischen den Wegen Frischluft→Kollektor→Server→Haus
(Winter) und Server→Kollektor→Außen (Sommer). Die Server-Lüfter (PWM) und
der Kollektor-Ventilator werden als eine Lüftergruppe gemeinsam geregelt.

### 6.3 Grenzen (ehrlich)

- **Gegendruck:** Lochblech + Filter kosten Druck; Server-Lüfter sind
  Hochdruck-Lüfter (gut geeignet), aber Volumenstrom messen (Anemometer,
  ~15 €) und per PWM abstimmen.
- **Staub:** Server-Lüfter im Kollektor-Kreis brauchen Vorfilter, sonst
  Lagerschaden – G4-Material, 2×/Jahr reinigen.
- **Luftdichtheit:** Undichte Kanäle verlieren die teuer errungene Wärme –
  Flexrohr mit Klemmringen, nicht nur Klebeband.

## 7. Integration ins Gesamtsystem

| Komponente | Kopplung |
|---|---|
| KWL (Frischluft, `06-…`) | Kollektor **vorheizt Zuluft**: statt −5 °C kommen +15 °C ins Haus – Frischluft, Pollenschutz und Gratis-Wärme in einem Strang |
| Pufferspeicher (`01-…`) | Luft-Wasser-Wärmetauscher lädt den Puffer – die Quelle für den 1–3-K-Hub-Betrieb der WP (`09-…`) |
| Wärmepumpe (`02-…`, `11-…`) | Weniger Last an kalten Sonnentagen; WP bleibt Lückenschließer |
| Netzfrei (`03-…`) | Regelt Volumenstrom nach Einstrahlung/Puffer-Temp, schaltet Sommer-/Wintermodus, misst Ertrag |
| **Server + Lüfter (`01-…`)** | **Server-EC-Lüfter als Kollektor-Antrieb (12 V/PWM/PV-Direkt), Server-Abluft (35–45 °C) als Wärmestufe im Luftkreis** (siehe Kap. 6) |
| Heizfolie/Farbe (`05-…`, `07-…`) | Kollektorwärme im Puffer + Folien-Spitzen = komplette Heizkette ohne fossile Energie |

**Kosten-Nutzen-Beispiel (15 m², gemäßigtes Klima):** Invest ~900 €,
Ertrag ~3.000–4.500 kWh/Jahr, Ventilator-Strom ~60 kWh/Jahr → Wärme für
unter 1 Cent/kWh über 20 Jahre. Keine andere Wärmequelle kommt auch nur
nahe daran.
