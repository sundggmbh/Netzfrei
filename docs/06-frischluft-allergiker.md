# 06 – Frischluft, Filter, Allergiker-Tauglichkeit

## 1. Warum kontrollierte Lüftung Pflichtteil des Systems ist

Ein gut gedämmtes Neubau-Gebäude ist luftdicht. Ohne kontrollierte Lüftung:
Feuchtigkeit, CO₂, Schimmel und Allergene. Mit kontrollierter Lüftung mit
Wärmerückgewinnung (KWL):

- **Frischluft ohne Wärmeverlust:** 85–95 % der Wärme der Abluft bleibt im Haus
  (Gegenstrom-Wärmetauscher). Im Winter heizt man nicht „das Fenster offen".
- **Im Sommer:** Bypass-Modus – nachts kühlt die Frischluft das Gebäude gratis
  (Freikühlung), tagsüber wird nicht nachgeheizt.
- **Entfeuchtung:** Koppelung an den Kühlkreis der Wärmepumpe (siehe
  `05-hybrid-strahlung.md`): Zuluft wird unter Taupunkt gekühlt, Kondensat läuft
  ab. Behagliche 40–55 % Luftfeuchtigkeit – wichtig gegen Milben und Schimmel.

## 2. Filterstufen (Allergiker-geeignet)

| Stufe | Filter | Filtert | Wechselintervall | Kosten |
|---|---|---|---|---|
| 1 | G4 Vorfilter | Grobstaub, Insekten, Pollen-Großanteil | 2–3 Monate | 5–10 € |
| 2 | **F7/F9 Feinfilter** | Pollen (>99 %), Feinstaub PM2.5/PM10, Ruß | 3–6 Monate | 15–30 € |
| 3 (optional) | HEPA H13 / Aktivkohle | Aerosole, Gerüche, Ozon | 6–12 Monate | 30–80 € |

**Für Allergiker:** F9-Filter entfernen >99 % der Pollen – das Gebäude wird
zur pollenfreien Zone in der Heuschnupfen-Saison. Zusätzlich: Pollenschutz-
gitter an der Lüftungsansaugung, keine Fensterlüftung nötig, Luftfeuchte
unter 55 % gegen Hausstaubmilben.

**Filterkosten gesamt: 40–100 €/Jahr** – verschmerzbar gegenüber der Ersparnis
durch Wärmerückgewinnung (bei 120 m² Neubau ~1.500–2.500 kWh Heizwärme/Jahr,
die sonst durch Fensterlüftung verloren ginge).

## 3. Auslegung

- **Luftwechsel:** 0,3–0,5 h⁻¹ (Neubau-Standard, DIN 1946-6 Lüftungskonzept).
- **Volumenstrom:** ~30 m³/h pro Person, 120 m²/4 Personen → 120–180 m³/h.
- **Geräteklasse:** Kompakt-KWL 150–250 m³/h mit Gegenstromtauscher;
  **Kosten 800–2.500 €** (DIY-Kits ab ~500 €).
- **Stromverbrauch:** 30–80 W im Dauerbetrieb (EC-Ventilatoren),
  ~300–600 kWh/Jahr – mit WRG netto stark positiv.
- **Kühlkopplung:** Nachgeschalteter Wasser-Luft-Wärmetauscher am Kühlkreis
  der WP (100–200 €) macht die KWL zur dezentralen Klimaanlage mit
  Entfeuchtung – ohne separates Split-Gerät.

## 4. KI-Steuerung der Lüftung

Das EMS regelt den Volumenstrom dynamisch:

| Situation | KWL-Modus |
|---|---|
| Anwesend, normal | Stufe 2 (Standard), CO₂-geregelt |
| Gäste / Kochen | Stufe 3 (Boost), automatisch via CO₂-/Feuchtesensor |
| Abwesend | Stufe 1 (Reduziert) |
| Pollensaison | Stufe 2 konstant, Filterüberwachung aktiv |
| Sommernacht, kühl draußen | **Bypass + Boost** → Gebäude auskühlen |
| Sommertag, heiß draußen | Mindestluft, Kühlung über Kühlkreis |
| Heizsaison, kalt | Stufe 2 mit WRG |

## 5. Kostenblock im Gesamtsystem (120 m²)

| Posten | DIY | Fachbetrieb |
|---|---|---|
| KWL-Gerät 150–250 m³/h | 500–1.200 € | 1.500–2.500 € |
| Luftleitungen/Verteiler (Neubau) | 300–600 € | 800–1.500 € |
| Kühlkopplung (Wasser-Luft-Tauscher + Ventil) | 150–300 € | 300–500 € |
| Filter (Jahresbedarf) | 40–100 €/Jahr | 40–100 €/Jahr |
| **Summe** | **~1.000–2.100 €** | **~2.600–4.500 €** |
