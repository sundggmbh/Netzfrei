# 09 – Kältemittel & minimaler Temperaturhub (1–3 K Betrieb)

## 1. Kältemittel-Recherche: Was wofür

| Kältemittel | GWP | Sicherheitsklasse | Einsatz heute | Für AUTARQ |
|---|---|---|---|---|
| **R290 (Propan)** | 3 | A3 (brennbar) | Haushalts-Kälte, Klimageräte, WP, Gewerbe | **Hauptkältemittel** – natürlich, überall verfügbar, billig (~10–20 €/kg), 70–75 °C Vorlauf möglich, 5 % Förderbonus (DE) |
| R744 (CO₂) | 1 | A1 (nicht brennbar) | Warmwasser, Hochtemperatur-WP, Gewerbe | Option für Warmwasser-Priorität; hoher Druck (~90–120 bar) = teurere Komponenten |
| R717 (Ammoniak) | 0 | B2L (giftig) | Industrie, große Anlagen | Nein (Toxizität im Wohnkontext) |
| R600a (Isobutan) | 3 | A3 | Haushaltskühlschränke | Bereits in unseren Kühlgeräten vorhanden |
| R718 (Wasser) | 0 | A1 | Vakuum-Dampfkälte, Forschung | Langfrist-Option für minimalen Hub (siehe unten) |
| R32 | 675 | A2L | Übergangslösung | Nein – **ab 2027 in neuen WP verboten** (EU 2024/573: GWP < 150) |
| R1270 (Propen) | 2 | A3 | wie R290 | Alternative zu R290 |

**Entscheidung für das Projekt: R290.** Gründe: natürlich (kein F-Gas, kein PFAS),
weltweit an jeder Ecke verfügbar (Industriegas, keine Mengenregulierung wie bei
synthetischen Kältemitteln), thermodynamisch auf Heizungsniveau gleichauf mit
R32 (ideell 1,3–2,3 % besser), selbst nachfüllbar für geschulte Selbstbauer,
Füllmengenbegrenzung (EN 378) durch kompakte Bauweise unkritisch (≤ 500 g).

## 2. Der Temperaturhub – der größte Effizienzhebel

**Physik:** COP ≈ η × T_verflüssigung / (T_verflüssigung − T_verdampfung).
Jede **1 K weniger Hub bringt 2–4 % mehr COP** (Kältetechnik-Faustregel).

**Belegte Messwerte (IEA HPT TCP, Forschung „Low-Lift"-Kältemaschinen):**

| Temperaturhub | COP (Heizen) | Quelle |
|---|---|---|
| 40 K (Standard-Luft/WP Winter) | ~4 | konventionell |
| 20 K (Erdsonde, gute Auslegung) | ~9 | IEA HPT Annex |
| **13 K** | **~11,4** | Meggers et al., Low-Lift-Chiller (gemessen) |
| 3 K (Ziel AUTARQ) | 12+ (praktisch begrenzt durch Verdichter-/Pumpenverluste) | Designziel |

**Warum unser System das kann – der Architektur-Trick:**

Konventionelle WP: Außenluft −5 °C → Vorlauf 40 °C = **45 K Hub**.
Unser System hält beide Seiten **warm und nah beieinander**:

```
Quelle (warm!):                    Senke (niedrig!):
  Pufferspeicher 19–22 °C            Fußboden/Kühldecke 22–26 °C
  ← geladen von:                     ← Strahlungsflächen (groß!)
    Server-Abwärme                     → 2–3 K reichen für Behaglichkeit
    Luftkollektor                      → ganzer Boden/Wand/Decke ist
    KWL-Abluft (5–8 °C Rest)             die Heizfläche
    Erdreich/Brunnen (8–14 °C)
```

**Hub: 2–3 K statt 45 K.** Bei 3 K Hub liegt der Carnot-COP bei ~100;
praktisch erreichbar sind **COP 8–15** – jedes kWh Strom wird zu 8–15 kWh Wärme.

## 3. Bautechnik für minimalen Hub (Designregeln für unsere WP)

| Maßnahme | Effekt | Kosten |
|---|---|---|
| **Überfluteter Verdampfer** (flooded evaporator) statt direkter Expansion | +16–48 % COP (Messreihen), gleichmäßige Benetzung | Plattenwärmetauscher + Abscheider, +100–200 € |
| **Übergroße Wärmetauscher** (Platten-WT, 2–3× Nenngröße) | Temperatur-Nähe Quelle/Senke ≤ 1–2 K statt 5–8 K | +150–300 € |
| **Ejektor statt Drosselventil** | Rückgewinnung von Drosselverlusten, +5–10 % | +50–150 € |
| **Inverter-Verdichter mit niedrigem Druckverhältnis** | kleine Hubs = kleine Druckverhältnisse = hoher Wirkungsgrad | Standard |
| **Große Strahlungsflächen im Gebäude** (Fußboden + Decke + Wandfolie) | Vorlauf 22–26 °C statt 35–45 °C | Heizfolie/Farbe (schon eingeplant) |
| **Wasser/Wasser statt Luft/Wasser** | Quelle konstant 8–22 °C, kein Abtauen | Erdsonde/Brunnen optional |

**Wasser (R718) als Kältemittel – Ausblick:** Bei Hubs von 1–3 K kann Wasser
selbst als Kältemittel arbeiten (Vakuum-Dampfkreis, Verdampfung bei ~10–20 °C
bei ~20–25 mbar). Kein GWP, keine Füllmengenlimits, unendlich verfügbar –
für Phase 2 des WP-Prototyps als Forschungszweig vorgemerkt.

## 4. Betriebsmodi mit minimalem Hub im Jahresverlauf

| Situation | Quelle | Senke | Hub | COP |
|---|---|---|---|---|
| Übergangszeit (Okt, Apr) | Puffer 18 °C (Server+Kollektor) | Fußboden 21 °C | **3 K** | 10–15 |
| Mildwinter (5–12 °C) | Erdreich/Puffer 10–14 °C | Fußboden 24 °C | 10–14 K | 8–11 |
| Kältewelle (−10 °C) | Außenluft −10 °C | Fußboden 30 °C | 40 K | 2,5–3,5 |
| Sommer Nacht | Gebäude 24 °C | Puffer 18 °C | 6 K | 8–12 (Kühlen) |
| Sommer Tag | Puffer 16 °C (Nacht geladen) | Kühldecke 19 °C | **3 K** | 10–15 (Kühlen) |

**Die KI minimiert den Hub in Echtzeit:** Sie lädt den Puffer mit allen Gratis-
Quellen (Server, Kollektor, Abluft, Erdreich) so warm wie möglich und hält die
Vorlauftemperatur so niedrig wie möglich – der Verdichter arbeitet dann fast nur
als „Temperatur-Feinjustierer". An den meisten Tagen des Jahres liegt der Hub
unter 10 K.

## 5. Konsequenz für die Auslegung

- Der WP-Verdichter kann **kleiner** ausgelegt werden (Spitzenlast nur bei
  Kältewellen): 3–5 kW statt 10 kW → billiger, leiser, Therme-Format leichter erreichbar.
- Die Batterie wird entlastet: Bei COP 10 statt 4 braucht die WP **60 % weniger
  Strom** → kleinere PV-/Batterie-Auslegung oder mehr Reserve.
- Der Pufferspeicher gewinnt an Bedeutung: Er ist die **Wärmequelle** der WP
  (nicht nur Speicher) – 500–1000 l, gut gedämmt, mit allen Gratis-Quellen
  gekoppelt.
