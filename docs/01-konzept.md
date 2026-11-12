# 01 – Systemkonzept

## 1. Zielbild

Ein Gebäude (Wohnung, Haus, Büro) wird mit einem geschlossenen System unabhängig vom
Stromnetz:

- **Strom** aus eigenen PV-Modulen (+ optional Kleinwindrad), gepuffert in einer Batterie.
- **Wärme** aus der kompakten Wärmepumpe, Solarkollektoren und der Abwärme von
  Servern, PCs, Kühlschränken und Tiefkühlschränken.
- **Kälte** aus derselben Wärmepumpe im Kühlbetrieb (reversibel), unterstützt durch
  nächtliche Freikühlung in gemäßigten Klimaten.
- **Steuerung** durch eine lokale KI (Energieleitsystem), die ohne Cloud funktioniert.

## 2. Energieflüsse (Gebäude als geschlossenes System)

```
                     ┌────────────────────────────┐
   Sonne ──► PV-Module ─┤                            ├──► Batterie ──► Haushaltsstrom
   Sonne ──► Kollektoren┤   PUFFERSPEICHER           ├──► Wärmepumpe (Verdichter-Strom)
                        │   (300–1000 l Wasser)      │
   Server/PC ──Abwärme──┤                            ├──► Fußbodenheizung (35 °C)
   Kühl-/TK-Schränke ──►┤  (Heizkreis oder Kühlkreis)├──► Warmwasser
                        └────────────────────────────┘
   Außenluft ──► Wärmepumpe ── Wärme/Kälte ──► Pufferspeicher
```

**Grundsatz:** Jeder Strom, der in einen Server, PC, Kühlschrank oder Tiefkühlschrank
fließt, wird zu 100 % Wärme. Im Heizfall ist diese Wärme also gratis nutzbar, wenn sie
über einen Wärmetauscher in den Pufferspeicher geleitet wird, statt den Raum aufzuheizen.

## 3. Komponenten

| # | Komponente | Auslegung (Richtwert) | Funktion | Kostenrahmen |
|---|---|---|---|---|
| 1 | PV-Anlage | 3–10 kWp, Dach/Fassade/Balkon | Eigene Stromerzeugung | 400–1.200 €/kWp |
| 2 | Batteriespeicher | 5–15 kWh | Nacht-/Winterversorgung | 150–400 €/kWh (Second-Life günstiger) |
| 3 | Kompakte Wärmepumpe | 1–10 kW modulierend, R290 | Heizen + Kühlen + Warmwasser | 3.000–6.000 € |
| 4 | Pufferspeicher | 300–1.000 l | Wärme-/Kältespeicher, Kopplung | 300–800 € |
| 5 | Homelab-Server | 200–800 W dauerlast | Rechenleistung + Abwärmeheizung | 500–1.500 € |
| 6 | Kühlschrank + Tiefkühlschrank | A+++/A++ | Kühlen/Einfrieren, Kondensatorwärme nutzbar | Standard |
| 7 | Solarkollektoren (thermisch, optional) | 2–6 m² | Direkte Warmwasser-/Heizunterstützung | 150–400 €/m² |
| 8 | **Netzfrei** (lokale KI, Heimnetzwerk) | Mini-PC/NUC im Homelab | Energieleitsystem: Messen, Steuern, Optimieren (siehe `03-…`) | 200–600 € |
| 9 | Fußbodenheizung / Kühldecke | 35 °C Heizung, 18 °C Kühlung | Niedertemperatur-Verteilung | Neubau-Standard |
| 10 | **Carbon-Heizfolie / IR-Paneele** | 8–20 €/m², 100–150 W/m² | Direkte Strahlungswärme, Zonenheizung (siehe `05-…`) | 1.000–2.500 € |
| 11 | **Lüftung mit Wärmerückgewinnung (KWL)** | 150–250 m³/h, F9-Filter | Frischluft, Pollenschutz, Entfeuchtung (siehe `06-…`) | 1.000–4.500 € |
| 12 | **Heizfarbe (Carbon)** | 24–48 V, 100–300 W/m², überstreichbar | Unsichtbare Strahlungsheizung durch Streichen (siehe `07-…`) | 10–15 €/m² |
| 13 | **Solar-Luftkollektor** | 30–80 €/m² DIY, 200–400 W/m² | Gratis-Wärme ab kurzer Sonneneinstrahlung (siehe `08-…`) | 600–1.200 € |
| 14 | Kühlgeräte-Abwärme-Kopplung | Kondensator → KWL/Brauchwasser | 450–600 kWh/Jahr Gratis-Wärme (siehe `08-…`) | 0–300 € |

## 4. Warum der Server das System trägt

- Ein Server mit 400 W Dauerlast liefert **3.500 kWh Wärme pro Jahr** – kostenlos,
  wenn er ohnehin läuft (KI-Rechenlast, NAS, Self-Hosting, BOINC/Folding@home).
- In einem Neubau mit 45 W/m² Heizlast reicht das allein für **bis zu 78 m²** im
  Übergangsbereich; die Wärmepumpe springt nur bei Kältespitzen zu.
- Im Sommer läuft die Rechenlast bevorzugt nachts/über Mittag, wenn PV-Strom im
  Überfluss vorhanden ist – die KI verschiebt die Last automatisch.

## 5. Klimazonen (weltweiter Einsatz)

| Zone | Beispiele | Heizlast | Kühlbedarf | Systemauslegung |
|---|---|---|---|---|
| **Kalt** | Nord-/Osteuropa, Gebirge | 60–100 W/m² | gering | Großer Pufferspeicher, WP mit hoher Vorlauftemperatur-Toleranz, PV-Auslegung auf Winter (steiler Dachwinkel), Server-Abwärme kritisch |
| **Gemäßigt** | Mitteleuropa | 35–55 W/m² | 10–30 W/m² (wenige Wochen) | Standardfall, reversibler Betrieb, Nachtauskühlung statt aktiver Kühlung |
| **Warm** | Südeuropa, MENA, Tropen | 0–20 W/m² | 40–80 W/m² | Kühlung dominiert: WP im Kühlbetrieb mit hoher SEER, PV-Auslegung auf Sommer, Solarkollektoren nur für Warmwasser, Server-Raum aktiv auf den Kühlkreis |

**Wichtig für heiße Klimate:** Die Server-Abwärme ist dort im Sommer ein *Problem*, das
gelöst werden muss – der Homelab wird daher an den Kühlkreis angeschlossen (wasser­gekühlt
über den Pufferspeicher), nicht an die Raumluft. Die KI entscheidet je nach Jahreszeit,
ob die Abwärme in den Heiz- oder Kühlkreis bzw. nach außen abgegeben wird.

## 6. Ein Haus, ein Netzwerk

Alle Aktoren hängen an einem Bus bzw. Mesh (Vorschlag: Thread/Zigbee + Powerline-
Ethernet für kritische Geräte):

- **Messung:** Stromzähler pro Kreis (PV, Batterie, WP, Server, Haushalt), Temperatur-
  sensoren pro Raum, Vor-/Rücklauf, Außentemperatur.
- **Aktoren:** Ventile/Umwälzpumpen der Heiz-/Kühlkreise, Dimmer/Schalter für Licht,
  smarte Steckdosen für verlagerbare Lasten (Waschmaschine, Spülmaschine, E-Auto-Lader).
- **Leitrechner:** Netzfrei, das Energieleitsystem (siehe `03-smart-home-ki.md`), entscheidet in
  1-Minuten-Takten über Erzeugung, Speicherung, Verbrauch und Verlagerung.

## 7. Hybrid-Prinzip: drei Hebeleben nach Kosten-Nutzen

Das System heizt und kühlt **hybrid** – immer über die billigste Quelle zuerst:

1. **Server-Abwärme + Solarkollektor** – kostenlos, Grundlast im Pufferspeicher.
2. **Wärmepumpe (COP 4–5)** – Fußboden-/Kühldecke als Grundtemperatur.
3. **Carbon-Heizfolie / Infrarot** – gezielt, sekundenschnell, nur wo Menschen
   sind; läuft bevorzugt direkt vom PV-Überschuss.

Strahlungswärme erlaubt 2–3 K niedrigere Lufttemperatur bei gleicher Behaglichkeit;
zusammen mit Zonen- und Anwesenheitssteuerung spart der Hybrid **25–40 %
Heizenergie** gegenüber einer reinen WP-Lösung – bei einer Zusatzinvestition von
nur 1.000–2.500 €. Details: `05-hybrid-strahlung.md`.

**Vierte Ebene – Gratis-Wärme ohne Strom:** Solar-Luftkollektoren (200–400 W/m²
schon bei kurzer Einstrahlung, DIY ab 30 €/m²), die Abwärme von Kühlschränken
und Tiefkühlschränken (450–600 kWh/Jahr pro Haushalt) und die KWL-Abluft als
WP-Wärmequelle liefern zusammen **8.500–11.000 kWh/Jahr** – fast der gesamte
Heizwärmebedarf eines Neubaus. Details: `08-waermequellen.md`.

## 8. Auslegungslogik (vereinfacht)

1. **Heizlast** = Wohnfläche × spezifische Last (abhängig von Baustandard und Klima).
2. **Kühllast** = Wohnfläche × Kühl-Faktor (abhängig von Klima).
3. **Warmwasser** = Personen × 1,6 kWh/Tag (60 °C-Äquivalent).
4. **Wärmepumpen-Leistung** = Heizlast − Server-Abwärmebeitrag, mindestens aber
   Kühlleistungsbedarf; modulierend 1–10 kW.
5. **PV-Größe** = Jahresbedarf (Strom + WP-Strom) ÷ spezifischer Ertrag der Zone.
6. **Batterie** = 50–70 % des täglichen Bedarfs (Abend-/Nachtdeckung).
7. **Pufferspeicher** = ≥ 10 l pro kW Heizlast, in kalten Zonen ≥ 15 l/kW.
