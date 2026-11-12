# 08 – Kostenlose Wärmequellen: Solar-Luftkollektoren & Kühlgeräte-Abwärme

## 1. Solar-Luftkollektor: Heizen schon bei kurzer Sonneneinstrahlung

Der einfachste und billigste Wärmeerzeuger überhaupt – **ohne Wasser, ohne
Frostschutz, ohne Pumpe**: Ein schwarzer Absorber hinter Glas/Polycarbonat,
Raumluft oder Frischluft strömt hindurch und kommt 17–28 K wärmer zurück.

**Recherche-Werte (DIY-praxisbelegt, u. a. BuildItSolar-Messreihen):**

| Kennwert | Wert |
|---|---|
| Wärmeleistung an klarem Wintertag | **200–400 W pro m²** |
| Baukosten DIY (Dose-/Sieb-Absorber, Holzrahmen, Polycarbonat) | **30–80 €/m²** |
| Fertiggerät (Transpired Collector / Luftkollektor) | 150–300 €/m² |
| Jahresertrag (Mitteleuropa, Südwand) | 200–350 kWh/m²/Jahr |
| Amortisation | oft 1–3 Jahre (DIY), 3–8 Jahre (fertig) |

**Warum er ins System passt:**
- Funktioniert **schon bei kurzer Einstrahlung** – klarer Wintervormittag genügt.
- **Keine Gefrierprobleme** (Luft statt Wasser) → ideal für kalte Klimazonen.
- Kopplung an die **KWL-Frischluft**: Der Luftkollektor **vorheizt die Zuluft**
  der Lüftungsanlage – im Winter kommt statt −5 °C Außenluft +15 °C ins Haus.
  Das ist die eleganteste Integration: Frischluft, Allergiker-Filter und
  Gratis-Wärme in einem Strang.
- Alternativ als Direkt-Luftheizung für Werkstatt/Garage/Hobbyraum.

**Auslegungsregel:** 1 m² Kollektor pro 5–10 m² Wohnfläche (Südwand/Dach);
bei 120 m² also 12–24 m² – realistisch sind an einer Südfassade 10–20 m²
ohne großen Aufwand.

## 2. Abwärme von Kühlschrank & Tiefkühlschrank

Kühlschränke geben am **Kondensator (Rückwand)** genau die Strommenge als Wärme
ab, die sie innen entziehen plus Kompressor-Strom:

| Gerät | Stromverbrauch/Jahr | Abwärme/Jahr |
|---|---|---|
| Kühlschrank A+++ (170 l) | ~90–120 kWh | ~90–120 kWh |
| Kühl-Gefrier-Kombi (250 l) | ~150–200 kWh | ~150–200 kWh |
| Tiefkühlschrank (200 l) | ~180–250 kWh | ~180–250 kWh |
| **Haushalt gesamt (3 Geräte)** | **~450–600 kWh** | **~450–600 kWh** |

**Integration (einfachste Variante zuerst):**
1. **Passiv (Standard):** Geräte in der Wirtschaftsküche/Technikbox aufstellen,
   Raumluft wird von der KWL als Abluft abgesaugt – die Wärme bleibt im
   Gebäude-Wärmehaushalt (über WRG sogar verwertbar).
2. **Aktiv:** Kondensator-Rückwand über einen Lüftungskanal mit dem
   **Luftkollektor-Rücklauf** koppeln: Kühle Kollektor-Rückluft kühlt den
   Kondensator → das Kühlgerät verbraucht **5–15 % weniger Strom** (bessere
   Kondensator-Kühlung), und die aufgenommene Wärme geht mit der Luft in die
   KWL-Zuluft-Vorwärmstrecke.
3. **Brauchwasser-Vorwärmung (Upgrade):** Kondensator-Wärme über einen
   Wärmetauscher an den Warmwasser-Vorlauf des Pufferspeichers –
   ~450–600 kWh/Jahr gratis ins Brauchwasser.

**Wichtig für heiße Klimate:** Im Sommer werden die Kühlgeräte an den
Kühlkreis-/Abluftstrom angeschlossen (siehe `01-konzept.md`, Kap. 5), damit
ihre Abwärme nicht ins Gebäude, sondern nach außen oder in den Warmwasser-
Speicher geht. Die KI schaltet die Kopplung saisonal um.

## 3. Abluft als Wärmequelle (vierte Ebene der Hybrid-Logik)

Die KWL-Abluft (20–22 °C) ist eine warme, konstante Quelle für die
Wärmepumpe: Nach dem Wärmetauscher der KWL hat die Abluft noch ~5–8 °C –
deutlich wärmer als Winter-Außenluft. Eine WP mit **Abluft-Ansaugung**
erreicht dadurch im Winter COP 4,5–5 statt 3,5–4.

**Kaskade im Gebäude:**

```
Raumluft (22 °C)
  → KWL-Wärmetauscher (heizt Zuluft vor, holt 85–95 % raus)
  → Rest-Abluft (5–8 °C) → WP-Verdampfer (letzte Wärme raus)
  → Ab Luft (−2 bis 0 °C) → Fortluft nach außen
```

Damit wird **jedes kWh Wärme dreimal genutzt**, bevor es das Gebäude verlässt.

## 4. Zusammengefasste Gratis-Wärmebilanz (120 m², gemäßigt, 4 Personen)

| Quelle | Wärme/Jahr | Kosten |
|---|---|---|
| Server-Abwärme (400 W) | ~3.500 kWh | 0 € (Server läuft ohnehin) |
| Solar-Luftkollektor 15 m² | ~3.000–4.500 kWh | 600–1.200 € einmalig |
| Kühlgeräte-Abwärme (3 Geräte) | ~450–600 kWh | 0–300 € (Kopplung) |
| Abluft-Nutzung (COP-Gewinn) | ~1.500–2.500 kWh WP-Ersparnis | 0–400 € (Ansaug-Umleitung) |
| **Summe Gratis-Wärme** | **~8.500–11.000 kWh/Jahr** | **≤ 1.900 € einmalig** |

Das entspricht **fast dem gesamten Heizwärmebedarf** eines Neubaus dieser
Größe (8.900 kWh/Jahr mit Hybrid-Folien) – die Wärmepumpe wird damit vom
Hauptwärmeerzeuger zum **Lückenschließer** an kalten, dunklen Tagen.
