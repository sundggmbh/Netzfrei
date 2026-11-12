# 13 – Produkt „SunWall": Der Sonnen-Luftkollektor als Marke

## 1. Produktidee

Der transpirierte Sonnen-Luftkollektor (schwarzes Lochblech, siehe
`12-sonnenluftkollektor.md`) wird zum **eigenen, professionellen Produkt**:

- **Positionierung:** das kostengünstige Solar-Heizsystem zum Selbstaufbau –
  professionelle Technik, faire Preise, online verkauft, weltweiter Versand.
- **Marken-Anschluss:** „**AUTARQ SunWall – powered by Netzfrei**"
  (Arbeitstitel; Alternativen: Sonnenwand, SunPerf, SolAir).
- **USP gegenüber dem Markt:** smart (Netzfrei-Integration, PV-Direkt-Ventilator,
  Messdaten), optimiert nach Forschungsstand (siehe unten), modular, DIY-tauglich
  mit richtiger Anleitung – und trotzdem im Preis bei DIY-Material.

## 2. Marktanalyse (Recherche-Stand)

| Anbieter | Profil | Preisniveau | Lücke, die SunWall füllt |
|---|---|---|---|
| **Grammer Solar** (Amberg, DE) | Premium, 45 Jahre Erfahrung, TwinSolar/SolarLuft, zertifiziert, staatlich gefördert, Anlagen bis mehrere 100 m² | hoch | Qualität zu fairem Preis |
| **SolarVenti** (SV3–SV30, Professional bis 80 m²) | Komplettsets, solarautark, Entfeuchtung/Lüftung/Heizung; SV30: 3,06 m², bis +40 K, ~2 kW, Räume bis 150 m² | mittel–hoch | Smart-Integration, offene Schnittstellen |
| **SolarWall** (Kanada) | Perforiertes Stahlprofilblech als Fassadensystem, Großprojekte | Projektgeschäft | Kleine Module für Haus/Wohnung |
| **Fernost-Importe** (div. Online-Shops) | Kleine Kollektoren, begrenzte Leistung, keine Dokumentation | niedrig | Leistung + Qualität + Anleitung + Support |
| **DIY-Szene** (BuildItSolar u. a.) | Belegte 30–80 €/m²-Bauten, kein Produkt | Materialpreis | Fertiges, geprüftes Bausatz-Produkt |

**Marktlücke:** Zwischen teurer Premium-Ware und leistungsschwachem Import-
Einzelteil fehlt ein **modulares, smartes, dokumentiertes Bausatz-System im
DIY-Preisband** – genau das ist SunWall.

**Hinweis Absatzmarkt Türkei:** mit ~1.500–1.700 kWh/m²·a Einstrahlung,
> 10 Mio. Gas-Heizungen (importabhängig) und kaum besetzter Luftkollektor-
Nische ist die Türkei zugleich Fertigungs- **und** Zielmarkt – Details in
`14-produktion-auftragsfertigung.md` Kap. 4.4.

## 3. Optimale Bauweise (aus der Forschung, Stand der Technik)

Die Kollektor-Forschung (40+ Jahre, u. a. Kutscher 1992, Gawlik/Kutscher 2002,
aktuelle Studien 2024/2025) kennt die Optimalparameter:

| Parameter | Optimum | Begründung |
|---|---|---|
| **Lochdurchmesser / Teilung** | **Ø 1 mm, 15 mm Raster** (Porosität ~0,3–1 %) | gemessen: Wärme-Übergangs-Effektivität ε > 0,70 über alle Volumenströme; >1 % Porosität = ungleichmäßige Absaugung |
| **Hinterluftraum (Plenum)** | **110 mm** (empfohlen 100–150 mm) | Druckrückgewinnung + gleichmäßige Strömung |
| **Glasabstand (Variante mit Glas)** | **30 mm** Absorber↔Glas | nahezu optimal gegen Konvektionsverluste, ohne Überhitzung (MDPI-Optimierungsstudie) |
| **Beschichtung** | mattschwarz, **Absorption α ≥ 0,95**; optional selektiv (niedrige Emission ε↓) | max. Sonnen-Aufnahme, min. Strahlungsverlust |
| **Wärmegewinn-Verteilung** | 62 % Vorderflächen-Grenzschicht, 28 % in den Löchern, 10 % Rückfläche | Lochblech nutzt alle drei – glatte Platte nicht |
| **Wind-Verluste (unglazed)** | gewellte/profilierte Bleche oder Glasabdeckung | Hauptverlustquelle bei offenen Kollektoren |
| **Volumenstrom** | 30–80 m³/h pro m², ventilatorgeregelt | niedrig = heißere Luft, hoch = mehr Gesamtwärme; Effizienz bis **84 %** bei hohem Strom (belegt) |
| **Effizienz-Vorteil TSC vs. glatter Absorber** | **+28–50 %** | Lochblech-Prinzip selbst |

**SunWall-Spezifik (Basismodul SW-2.0):**

| Merkmal | Wert |
|---|---|
| Modulformat | 1.000 × 2.000 × 130 mm (B×H×T), ~18 kg |
| Absorber | Alu/Stahl-Lochblech, Ø 1 mm / 15 mm Raster, mattschwarz α ≥ 0,95 |
| Plenum | 110 mm, innen gedämmt (30–50 mm), dicht (Dichtheits-Prüfkriterium) |
| Varianten | **SW-U** (unglazed, windarm profiliert) / **SW-G** (4-mm-Glas, 30 mm Abstand, +15–20 % Ertrag) |
| Ventilator | EC-Radial 10–25 W, PWM, **12/24 V PV-Direkt** (kein Wechselrichter) |
| Anbindung | PWM-Eingang + Modbus/ESPHome (Temperatur vor/nach, Strömung, Ertrag) → Netzfrei |
| Leistung (SW-G, 2 m²) | 400–800 W an klarem Wintertag, ΔT bis 40 K |
| Jahresertrag | 400–700 kWh pro Modul (Mitteleuropa, Süd) |
| Montage | Wand/Fassade/Dach, Modul-Kupplung zu Wänden (2–30+ Module) |
| Ziel-Verkaufspreis | **SW-U: 249–349 €/Modul, SW-G: 349–449 €/Modul** (Bausatz, inkl. Ventilator + Anleitung) |

## 4. Produktlinien

| Produkt | Zielgruppe | Preisband |
|---|---|---|
| **SW-1.0 Starterkit** (1 m², unglazed) | Mietwohnung, Balkon, Wochenendhaus | 149–199 € |
| **SW-2.0 Basismodul** (2 m², U/G) | Einfamilienhaus, Büro | 249–449 € |
| **SW-Wand** (4–10 Module + Kanäle) | Haus-Heizungsunterstützung + KWL-Vorwärmung | 1.200–4.500 € |
| **SW-Pro** (20–100 m²) | Gewerbe, Lager, Trocknung (Holz/Heu/Getreide), Agrar | 6.000–30.000 € |
| **Zubehör** | PV-Direkt-Ventilator-Set, KWL-Kopplungsset, Puffer-Luft-WT, Mess-Kit | 30–250 € |

## 5. Qualität & Technik-Feinschliff (Plan)

1. **Prüfstand:** Pyranometer (~50 €), T-Sensoren vor/nach, Anemometer,
   Datenlogger → Wirkungsgrad-Kennlinie je Modul; jede Fertigungscharge wird
   stichproben-geprüft, Messprotokoll liegt dem Produkt bei („Ihr Modul hat
   bei 800 W/m² X kWh Wärme geliefert").
2. **Dichtheits-Standard:** Plenum-Dichtheitsprüfung als QC-Schritt
   (Undichtigkeit = der häufigste Ertragskiller bei DIY).
3. **Wind-Stabilität:** profilierte Lochblech-Variante nach Gawlik/Kutscher
   (Wind-Verluste −30–50 %).
4. **Selektivbeschichtung testen** (α ≥ 0,95 / ε < 0,30): +10–15 % Ertrag,
   Kostenaufwand prüfen – Entscheidung nach Prototyp-Messung.
5. **Zertifizierung:** Solar-Keymark-Anschluss für Luftkollektoren prüfen
   (Voraussetzung für staatliche Förderung vieler Länder – Verkaufsargument).
6. **Netzfrei-Integration als Alleinstellung:** Jedes Modul meldet Ertrag und
   Status; die KI optimiert Volumenstrom, Sommer-/Wintermodus, Koppelung an
   KWL/Puffer/WP. Kein Wettbewerber hat das.

## 6. Vermarktungs-Architektur (Internet)

- **Verkaufskanäle:** eigener Onlineshop (Bausätze + Module), eBay/Etsy/Amazon
  für Starterkits, B2B-Marktplätze für Agrar/Trocknung (SW-Pro).
- **Zielgruppen:** Selbstbauer & Homesteader, Ferienhäuser/Werkstätten,
  Agrar-Trocknung, Off-Grid-Communities, Länder mit hohen Heiz-/Lüftungskosten
  und viel Sonne (Ost-Europa, Zentralasien, Anden, Nordamerika).
- **Content-Strategie:** Messdaten & Bauanleitungen offen publizieren
  (GitHub/Open-Hardware) = Vertrauen + SEO; YouTube-Bautagebücher;
  Kernbotschaft: „**Wärme für unter 1 Cent/kWh**".
- **Preis-Logik:** Material × 1,5–2 (Bausatz) bzw. × 2,5–3 (fertig) – fair
  gegenüber der DIY-Szene, tragfähig für Serienfertigung.
- **Fertigung:** Start mit Lohnfertigung (Blechzentrum + Beschichtung +
  Bausatz-Montage), ab ~500 Modulen/Jahr eigene Fertigung wirtschaftlich –
  Details, Standorte, Materialpreise und Fördermittel: siehe
  `14-produktion-auftragsfertigung.md`.

## 7. Roadmap zum Produkt

- [ ] **P1 – Referenz-Prototyp:** 3 Module (SW-U, SW-G, SW-G selektiv) bauen,
      Prüfstand aufbauen, Kennlinien messen (4–6 Wochen)
- [ ] **P2 – Design-Freeze:** beste Variante, Stückliste, Fertigungszeichnungen,
      Montageanleitung
- [ ] **P3 – Kleinserie:** 20–50 Module, Beta-Kunden (Werkstatt, Ferienhaus,
      Agrar), Feldmessdaten sammeln
- [ ] **P4 – Shop & Marke:** Onlineshop, Name/Logo final, Solar-Keymark-Prozess
- [ ] **P5 – Skalierung:** SW-Pro-Linie, internationale Märkte, Netzfrei-Bundle
      (Kollektor + EMS als Komplettpaket)
