# 07 – Heizfarbe: Heizen durch Streichen (Carbon-Schwarzfarben)

## 1. Recherche-Ergebnis: Heizfarbe ist marktreif

Elektrisch leitfähige Farben mit Carbon-/Graphit-Anteilen existieren als
Serienprodukte:

| Produkt / Anbieter | Technik | Daten |
|---|---|---|
| **Carbo e-Paint** (FutureCarbon, Bayreuth) | wasserbasierte, schwarze Dispersion mit Carbon-Partikeln | 24 V Niederspannung, bis ~300 W/m², überstreichbar, wenige Minuten Aufheizzeit |
| **Rebotherm Energy Heizfarbe** | Carbon-Heizbeschichtung (+ Folien, Aerogel-Dämmung) | 24–48 V, bis ~350 W/m², Schichtdicke ~0,2 mm, TÜV-Zertifizierung angegeben |
| **Heizputz/Heizlack-Varianten** | Carbonfasern im Putz/Lack (patentiert, DE202014009744U1) | Niederspannung, direkt an Kältebrücken einsetzbar |

**Prinzip:** Carbon-Partikel in der Farbschicht leiten Strom; der elektrische
Widerstand der Schicht erzeugt Wärme (Joule-Effekt). Die Farbe wird schwarz
aufgetragen (Kupfer-Busbar-Elektroden oben/unten), danach **überstreicht man
sie ganz normal** – die Heizfläche ist unsichtbar. Abgabe als langwellige
Infrarot-Strahlung, wie bei Heizfolie.

## 2. Warum das ins AUTARQ-System passt

- **Billigste Heizfläche überhaupt:** Materialaufwand pro m² liegt im Bereich
  von Wandfarbe plus Elektroden; keine Geräte, keine Hydraulik, kein Wartungsfall.
- **Selbst machbar:** Streichen statt installieren – Malerqualität genügt,
  entscheidend ist gleichmäßige Schichtdicke und saubere Elektroden-Kontaktierung.
- **24/48 V Niederspannung:** direkt aus PV + Batterie über DC-Bus speisbar,
  kein Wechselrichter-Verlust, keine Elektrofachfirma für die Flächen nötig
  (nur der Anschluss an den DC-Bus/Netzteil).
- **KI-ideal:** Reaktion in Minuten statt Stunden – perfekte Aktorik für
  Anwesenheits- und PV-Überschuss-Steuerung (gleiche Logik wie Heizfolie,
  siehe `05-hybrid-strahlung.md`).
- **Kältebrücken-Heiler:** In Altbauten direkt an kalten Wandecken streichen →
  keine Kondenszonen, kein Schimmel.

## 3. Risiken / ehrliche Einordnung

- **Gleichmäßigkeit:** Uneinheitliche Schichtdicke = Hotspots. Lösung: Auftrag
  mit Airless-Sprühgerät oder Quetschvorrichtung, Abnahmemessung mit
  Widerstandsmessung pro Feld.
- **Verarbeitung** wird von Herstellern als schulungsbedürftig eingestuft –
  für das AUTARQ-Projekt heißt das: Bauanleitung + Prüfprotokoll (Widerstand
  pro m² vor Überstreichen) in die Open-Hardware-Doku.
- **COP 1:** Wie Folie reine Widerstandswärme – der Wert liegt in der gezielten
  Anwendung und der direkten PV-Speisung, nicht im Wirkungsgrad.
- **Zertifizierung prüfen:** Beim Kauf TÜV-/CE-Nachweis verlangen;
  Eigenansätze nur mit RCD/FI-Schutz und Niederspannung (< 48 V).

## 4. Rollenverteilung im System (mit Folie/IR zusammen)

| Ebene | Technik | Aufgabe |
|---|---|---|
| Grundwärme | WP + Fußboden (35 °C) | Basis-Temperatur Gebäude |
| Zonen-Komfort | **Heizfarbe** (Wand/Decke, unsichtbar) | Dauerzonen: Bad, Büro, Schlafzimmer |
| Schnell-Komfort | IR-Paneele / Heizfolie | Burst-Heizung bei Anwesenheit, Mietwohnungen |
| Gratis-Wärme | Server-Abwärme, Luftkollektor (`08-…`) | Grundlast ohne Stromkosten |

## 5. Kosten (120 m² Wohnung, ~40 m² beheizte Wandfläche)

| Posten | Kosten |
|---|---|
| Heizfarbe 40 m² (2 Schichten) | 300–700 € (Material) |
| Kupfer-Busbar-Elektroden, 24-V-Netzteile/DC-Bus | 150–300 € |
| Zonen-Thermostate/Aktoren (4 Zonen) | 100–200 € |
| **Summe** | **~550–1.200 €** |

Vergleich Heizfolie (~20 €/m², schneller verlegbar, robust) vs. Heizfarbe
(~10–15 €/m², unsichtbar, nachrüstbar in Mietwohnungen): Im Neubau kombinieren
wir beides – **Folie unter dem Bodenbelag der Hauptaufenthaltsflächen, Farbe an
Wand/Decke der Nebenzonen**.
