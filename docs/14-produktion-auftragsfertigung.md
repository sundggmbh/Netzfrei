# 14 – SunWall-Produktion: Auftragsfertigung, Beschaffung, Standorte, Fördermittel

Wie aus dem Prototyp (`13-produkt-sunwall.md`) ein **Produkt unter eigenem
Markennamen** wird, ohne ein eigenes Werk zu bauen: Fertigung wird eingekauft
(Auftragsfertigung / Lohnfertigung / Private Label), **Marke, Konstruktion und
Vertrieb bleiben bei uns**.

## 1. Grundprinzip: Wir besitzen Marke + Wissen, nicht die Maschinen

```
                 bleiben bei uns                    wird eingekauft
  ┌────────────────────────────────┐   ┌─────────────────────────────────┐
  │  Marke „SunWall“ (DPMA/EUIPO)  │   │  Blechteile (Lasern/Stanzen,    │
  │  Konstruktion & Zeichnungen    │──▶│  Biegen, Pulverbeschichtung)    │
  │  Prüfstand & Spezifikation     │   │  Rahmen (Alu-Zuschnitt)         │
  │  Netzfrei-Firmware/Elektronik  │   │  Elektronik (SMD-Bestückung)    │
  │  Onlineshop, Vertrieb, Support │   │  Endmontage/Konfektionierung    │
  │  Qualität & Zuliefererauswahl  │   │  Logistik/Versand (3PL möglich) │
  └────────────────────────────────┘   └─────────────────────────────────┘
```

Damit ist SunWall ein **„asset-light“-Produkt**: Kapital geht in Prototyp,
Prüfstand, Zertifizierung und Marketing – nicht in Maschinenpark und Miete.

## 2. Make-or-Buy: drei Stufen

| Stufe | Modell | Volumen | Investition | Stückkosten-Hebel | Risiko |
|---|---|---|---|---|---|
| **A – Werkstatt-Selbstbau** | eigene Garage/Werkstatt, 1–2 Personen | 1–50 Module | ~3.000–8.000 € (Handwerkzeuge, Schere, Kantbank gebraucht) | hoch (keine Skalierung) | gering; begrenzt Zeit |
| **B – Lohnfertigung verteilt** (empfohlener Einstieg) | Blechzentrum + Pulverbeschichtung + SMD-Dienstleister + eigene/externe Endmontage | 50–2.000 Module/Jahr | ~5.000–15.000 € (Werkzeuge, Vorrichtungen, Erstmustermuster) | gut (Serienpreise ab 50 Stück) | mittel; Qualitätskontrolle nötig |
| **C – Full-Contract-Manufacturer** | ein Partner fertigt komplett „unter unserer Marke“ (inkl. Einkauf) | ab ~1.000–5.000 Module/Jahr | gering (aber Mindestmengen, Werkzeugkosten) | am besten | hoch; Abhängigkeit, IP-Schutz nötig |

**Empfehlung:** Start mit **Stufe B** – bereits ab 20–50 Modulen realistisch,
keine Mindestmengen bei regionalen Blechzentren, volle Kontrolle über
Qualität (siehe Prüfstand, `13-produkt-sunwall.md` Kap. 5). Stufe C erst,
wenn der Markt Mengen von >1.000 Modulen/Jahr trägt.

## 3. Fertigungsaufteilung pro Modul (SW-2.0, Bausatz)

| Baugruppe | Wer fertigt | Verfahren | Anmerkung |
|---|---|---|---|
| Absorber-Lochblech (Ø 1 mm / 15 mm Raster) | Blechzentrum/Laserdienstleister | Laser- oder Stanz-Nibbeln, dann Biegen | Kernstück; Werkzeug beim Stanzen günstiger ab ~500 Stück |
| Rückwand + Plenum-Wände | Blechzentrum | Lasern + Biegen | Standard-Alu/Stahlblech 0,8–1,5 mm |
| Beschichtung (mattschwarz α ≥ 0,95) | Pulverbeschichter (Lohn) | Pulverbeschichtung mattschwarz | selektive Beschichtung (Stufe SW-G selektiv) nur über Spezialdienstleister |
| Dämmung (30–50 mm) | Zukauf Standard | Mineralwolle/PUR-Schnitte | kein Sonderteil |
| Glas/Stegplatte (SW-G) | Zukauf Standard | 4-mm-Einscheibensicherheitsglas oder 16-mm-Stegplatte | Zuschnitt beim Glaser/Plattenhändler |
| Alu-Rahmen/Profile | Zukauf + Zuschnitt | Standard-Systemprofile (30×30 o. ä.) | kein Sonderwerkzeug nötig |
| EC-Ventilator 12/24 V PWM | Zukauf (Großhandel/Direktimport) | – | siehe `12-sonnenluftkollektor.md` Kap. 6 |
| Elektronik (ESP32, PWM, Sensorik) | SMD-Dienstleister | Bestückung nach unseren Plänen | Leiterplatten + Montage ab ~10 Stück wirtschaftlich |
| Dichtungen, Schrauben, Kabel | Zukauf Standard | – | – |
| **Endmontage + Verpackung** | **wir** (Stufe B) oder Fertiger (Stufe C) | Konfektionierung | Bausatz = Teile + Anleitung; fertig = montiert |

**Wichtig:** Der Bausatz-Ansatz reduziert den Montageaufwand drastisch –
Endmontage durch den Kunden ist Teil der Positionierung („fairer Preis,
richtige Anleitung“) und spart Lohnkosten.

## 4. Standortvergleich: Deutschland vs. Türkei vs. Osteuropa

### 4.1 Recherche-Befund

- **Türkei (Istanbul/Bursa/Izmir/Marmara-Region):** das industrielle Zentrum
  (Bursa/Kocaeli = Automobil-Zulieferindustrie) hat eine dichte Landschaft von
  ISO-9001-zertifizierten Blechbearbeitern mit Lohnfertigung nach Zeichnung,
  teils mit 48-h-Angebot und 5–7 Tagen Lieferung nach Deutschland; Einkaufs-
  Sparpotenzial wird mit **10–60 %** gegenüber deutschen Preisen angegeben.
- **EU-Zollunion (seit 1996):** gewerbliche Waren zwischen EU und Türkei sind
  **zollfrei**, Nachweis ist die **Warenverkehrsbescheinigung A.TR** (kein
  Ursprungsnachweis nötig); paneuropäische Ursprungskumulierung möglich.
  Ausgenommen: Agrar- und EGKS-Waren (Kohle/Stahl) – für Standard-Blechteile
  relevant prüfen, ob Kapitel-72-Stahlwaren betroffen sind.
- **Deutschland:** höchste Lohnstundenkosten, aber kürzeste Wege, kein
  Währungsrisiko, einfache Gewährleistung, „Made in Germany“ als Verkaufs-
  argument, Förderzugang (Kap. 7).
- **Osteuropa (Polen/Tschechien/Slowakei):** Zwischenposition – EU-Binnenmarkt
  (kein Zoll, keine A.TR), Lohnkosten deutlich unter Deutschland, gute
  Blech- und Kunststoffindustrie, 1–2 Tage LKW-Logistik nach DE.

### 4.2 Vergleich (relative Kosten, Blechteile + Montage = 100 % Basis DE)

| Kriterium | Deutschland | Türkei (Marmara/İzmir) | Polen/Tschechien |
|---|---|---|---|
| Lohn-/Fertigungskosten | 100 % | ~35–55 % | ~55–70 % |
| Zoll/Handelshemmnis | – | **0 % Zoll** (A.TR), Zollpapierkram | 0 % (Binnenmarkt) |
| Logistik nach DE | 1–2 Tage | 3–7 Tage LKW | 1–2 Tage LKW |
| Währungsrisiko | – | **ja (TRY)** → in EUR kontrahieren | gering (PLN/CZK) |
| Qualitätsmanagement | einfach (vor Ort) | Aufwand (Audits, Erstbemusterung) | einfach–mittel |
| Mindestmengen | niedrig | mittel–hoch | niedrig–mittel |
| „Made in …“-Argument | stark | neutral | neutral |
| Förderzugang (DE-Unternehmen) | voll (Kap. 7) | nur indirekt | nur über Landesprogramme |

### 4.3 Empfehlung (Staffelung nach Menge)

| Phase | Fertigungsstandort | Begründung |
|---|---|---|
| P1–P2 Prototyp + Design-Freeze | **Deutschland** (lokale Werkstatt + Blechzentrum) | schnelle Iteration, Prüfstand nebenan |
| P3 Kleinserie 20–50 Module | **Deutschland oder Polen** | Vorrichtungen aufbauen, Qualität etablieren |
| P4–P5 ab ~500 Module/Jahr | **Türkei für Blechteile** (Laser/Stanz/Biegung/Beschichtung), Endmontage + Elektronik in DE | größter Kostenblock (Blech) günstig, Endmontage bleibt qualitätskontrolliert nahe am Kunden |

**Hybrid-Modell als Default:** teure, tolerance-kritische Teile (Absorber-
Lochblech, Elektronik) zuerst EU-nah; einfache Teile (Rückwand, Rahmen,
Dämmung, Verpackung) dort, wo sie am günstigsten sind.

Auch die **Firmensitz-Frage** (Türkei-Steuerprogramm 2026) gehört in diese
Entscheidung – siehe Kap. 8.

## 5. Materialbeschaffung: Stückpreise nach Menge

Alle Werte sind Markt-Erfahrungswerte (Blechhandel, Großhandel, Direktimport),
**zu verifizieren per RFQ** (Kap. 6). Basis: Modul SW-2.0 (2 m² Absorber,
Rahmen, Ventilator, Elektronik, Dämmung).

| Material | Quelle | 50 Stück | 500 Stück | 5.000 Stück |
|---|---|---|---|---|
| Lochblech Alu/Stahl 1,0–1,5 mm, Ø 1 mm/15 mm | Blech-Servicezentrum; ab ~500 Stück Walzwerk-Sonderanfertigung | 45–70 € | 30–45 € | 18–28 € |
| Rückwand + Plenum (Blech, gebogen) | Blechzentrum | 30–50 € | 18–30 € | 10–18 € |
| Pulverbeschichtung mattschwarz | Lohnbeschichter | 15–25 € | 8–15 € | 4–8 € |
| Dämmung 30–50 mm | Baustoffhandel | 10–18 € | 6–10 € | 4–7 € |
| Glas 4 mm / Stegplatte 16 mm | Glaser/Plattenhandel | 25–45 € | 15–25 € | 9–15 € |
| Alu-Rahmenprofile + Ecken | Systemprofil-Händler | 20–35 € | 12–20 € | 7–12 € |
| EC-Ventilator 12/24 V, 10–25 W PWM | EU-Großhandel vs. Direktimport (MoQ 500–1.000) | 25–60 € | 12–25 € | 6–12 € |
| Elektronik (Platine + ESP32 + Sensoren, bestückt) | SMD-Dienstleister (EU oder Asien) | 18–30 € | 9–15 € | 5–9 € |
| Kleinteile (Dichtung, Schrauben, Kabel, Gitter) | Großhandel | 10–20 € | 6–12 € | 3–6 € |
| Verpackung (Wellpappe, Europalette-Anteil) | Verpackungshandel | 8–15 € | 5–8 € | 3–5 € |
| **Material gesamt/Modul** | | **~210–370 €** | **~120–200 €** | **~70–120 €** |

**Interpretation gegen die Ziel-Verkaufspreise** (SW-U 249–349 €,
SW-G 349–449 €, siehe `13-produkt-sunwall.md`):

- Bei 500 Stück liegt der Materialaufwand bei ~50–60 % des Verkaufspreises
  (SW-U) – mit Zuschlag für Fracht, Zoll-Papierkram, Ausschuss, Garantie,
  Marketing bleibt eine Marge von ~20–35 %. **Realistisch, aber knapp.**
- Ab 5.000 Stück wird die Marge komfortabel (~50–70 % Brutto) – das ist die
  Schwelle, ab der sich Stufe C (Full-Contract-Manufacturer) lohnt.
- **Hebel Nr. 1 ist der Ventilator** (Direktimport halbiert den größten
  Zukaufposten), **Hebel Nr. 2 das Lochblech** (Sonderanfertigung ab ~500
  Stück deutlich billiger als Einzelzuschnitt).

## 6. Hersteller-Anforderungsprofil (RFI/RFQ-Vorlage)

Kopiervorlage für die Erstansprache von Blechzentren, Beschichtern, SMD-
Dienstleistern und Contract-Manufacturern:

```
ANFRAGE Lohnfertigung – Sonnen-Luftkollektor „SunWall“ (Modul 1.000 × 2.000 mm)

1. Unternehmen
   - Ansprechpartner, Standort, Zertifizierungen (ISO 9001, ggf. EN 1090)
   - Referenzen im Bereich Solartechnik / HLK / Metallbau

2. Leistungsumfang (Bitte ankreuzen)
   [ ] Lasern/Stanzen + Biegen (Blechteile nach DXF)
   [ ] Pulverbeschichtung mattschwarz RAL 9005, Schichtdicke 60–80 µm
   [ ] Selektive Absorberbeschichtung (falls verfügbar)
   [ ] Endmontage nach Montageanleitung (Konfektionierung)
   [ ] Komplettfertigung inkl. Materialbeschaffung (Contract Manufacturing)

3. Teile (Zeichnungen/DXF liegen bei)
   - Absorber-Lochblech: Ø 1 mm, Raster 15 mm, 1.000 × 2.000 mm, Alu/Stahl
   - Rückwand + Plenum-Wände: 0,8–1,5 mm
   - Stückzahlen: Erstlos 20 / 50, Jahresbedarf 200–2.000

4. Anforderung
   - Toleranzen: ±1 mm (Rahmen), Lochraster ±0,5 mm
   - Erstbemusterung vor Serie (2 Muster, kostenpflichtig)
   - Rückmeldung zu: Stückpreis je Menge, Werkzeugkosten, Lead-time,
     Mindestbestellmenge, Lieferung (DDP Deutschland)

5. Rahmen
   - Auftragsfertigung nach unseren Zeichnungen; Werkzeuge gehen in unser
     Eigentum über; Vertraulichkeit (NDA) vor Zeichnungsübergabe
   - Zahlungsziel, Gewährleistung, Ausschuss-Regelung (max. 2 %)
```

**Auswahlkriterien (gewichtet):** Qualität/Erstmuster (30 %), Preis (25 %),
Zuverlässigkeit/Lead-time (20 %), Kommunikation (15 %), Standort/Logistik
(10 %). Erst nach NDA Zeichnungen herausgeben.

## 7. Fördermittel (Deutschland/EU, Recherche-Stand)

| Programm | Was | Umfang | Passung zu SunWall |
|---|---|---|---|
| **KfW ERP-Gründerkredit StartGeld (067)** | zinsgünstiger Kredit für Gründung/junge Firmen (< 5 Jahre), Hausbank-Verfahren | bis **200.000 €** (Höchstbetrag Dez. 2025 von 125.000 auf 200.000 € angehoben), 80 % Haftungsfreistellung | Erstausstattung Werkstatt, Erstserie, Prüfstand |
| **KfW ERP-Gründerkredit Universell (068)** | Investitionen + Betriebsmittel | bis 25 Mio. € | Skalierungsphase P5 |
| **Gründungszuschuss** (Agentur für Arbeit) | Existenzgründung aus ALG I | 6 Monate ALG I + 300 €, Verlängerung möglich | Persönliche Absicherung in der Gründungsphase |
| **EXIST-Gründerstipendium** | Gründung aus Hochschule | Stipendium + Sachmittel | nur mit Hochschul-Anbindung |
| **Forschungszulage** (FZulG) | steuerliche F&E-Förderung | ~25 % Personalkosten-Zuschuss (KMU-Erhöhung), bis 690.000 € förderfähige Einzelkosten | P1-Prüfstand + Kennlinien-Messungen (wir betreiben F&E) |
| **ZIM** (Zentrales Innovationsprogramm Mittelstand) | Technologie-/Innovationsprojekte | Zuschuss ~60 % (Richtlinie V5, ab 2025), bis ~690.000 € förderfähige Kosten | Weiterentwicklung Absorber/Selektivbeschichtung + Netzfrei-Regelung |
| **BAFA-Modul „Energieberatung“ / Mittelstand-Digital** | Beratungs- und Digitalisierungs-Zuschüsse | bis ~4.000 € bzw. 50 % | Onlineshop/ERP-Aufbau, Fertigungs-Digitalisierung |
| **INVEST – Zuschuss für Wagniskapital** | Erleichtert Business-Angel-Finanzierung | 20 % Kaufpreis-Zuschuss | Wenn Wachstumskapital geholt wird |
| **EU: EIC Accelerator / Horizon Europe** | Deep-Tech-Innovation | Zuschuss + Eigenkapital, hoch kompetitiv | erst ab validiertem Produkt (P4/P5) |
| **Landesförderbanken** (NRW.BANK, L-Bank, LfA, IBB …) | regionales Gründungs-/Innovationsdarlehen | je nach Land | ergänzend zur KfW, oft kombinierbar |

**Praktischer Pfad:** (1) Gründungszuschuss/StartGeld für die Gründungsphase,
(2) Forschungszulage für den Prüfstand (P1), (3) ZIM für die Weiterentwicklung
(P3/P4), (4) ERP-Universell für die Skalierung. **Wichtig:** Programme sind
teilweise kombinierbar, aber **De-minimis-Grenzen** tracken; Hausbank ist bei
KfW-Krediten immer der erste Ansprechpartner.

## 8. Türkei als Firmensitz: Steuer-Programm 2026 und Realitätscheck

### 8.1 Was tatsächlich angekündigt wurde (Recherche-Stand)

Im April 2026 hat die Türkei das Programm „Türkiye Yüzyılı – Strong Center for
Investment" (Strong Investment Hub Program) angekündigt; Teile sind als Gesetz
Nr. 7582 bzw. neuer Art. 20/D EStG (TR) in Kraft bzw. auf dem Weg ins Parlament:

| Maßnahme | Inhalt | Bedingung/Einschränkung |
|---|---|---|
| **20 Jahre Steuerbefreiung für Auslands-Einkünfte** | Zuziehende Personen zahlen keine türkische Steuer auf **ausländische** Einkünfte (Dividenden, Veräußerungsgewinne, Vermietung) | Nur für Personen, die in den letzten 3 Jahren **nicht** türkische Steuerresidenten waren; Erbschaft/Schenkung 1 % |
| **95–100 % Befreiung Regional-HQ** | Gewinne aus regionalen Hauptquartier-/Management-Funktionen, 20 Jahre | gilt für die HQ-Tätigkeit, nicht pauschal fürs ganze Unternehmen |
| **Reduzierte KSt für Exporteure** | angekündigt ~9 % Körperschaftsteuer für Fertigungs-Exporteure | **Ankündigung**, Gesetzestext/Details offen; Inlandsumsatz nicht befreit |
| **Transit-Handel / IFC** | nahezu vollständige Befreiung; Istanbul Finance Centre: Fee-Befreiung 5 → 20 Jahre | betrifft Handels-/Finanzplätze, nicht Fertigung |
| **One-Stop-Shop** | Firmengründung, Arbeitserlaubnis, Genehmigkeiten über eine digitale Plattform (Presidential Investment Office) | Verwaltungsvereinfachung |
| **Technoparks (Law 4691)** | KSt-Befreiung für Software-/F&E-Erlöse aus der Zone (bis 31.12.2028) | nur Software/R&D-Erlöse, nicht Hardware-Verkauf |

### 8.2 Was das NICHT bedeutet (ehrlicher Realitätscheck)

- **Kein Pauschal-„0 % Steuern" für umgezogene deutsche Fertigungsfirmen.**
  Die großen Befreiungen zielen auf (a) Auslands-Einkünfte von **Personen**,
  (b) Regional-HQ-Funktionen, (c) Transit-/Finanzgeschäft. Wer in der Türkei
  **produziert und verkauft**, zahlt dort reguläre Körperschaftsteuer
  (~25 % Standard; 9 % für Exporteure nur angekündigt).
- **Deutschland bleibt angekoppelt:**
  - DBA Deutschland–Türkei (2011) verteilt die Besteuerungsrechte; die
    Ansässigkeit entscheidet, nicht der Satzungssitz allein – der **Ort der
    Geschäftsleitung** zählt.
  - Bleibt in Deutschland ein **Lager, Montage oder Service** (unser
    Hybrid-Modell, Kap. 4.3), ist das eine **deutsche Betriebsstätte** – die
    dazugehörigen Gewinne bleiben in DE steuerpflichtig.
  - **Wegzugsbesteuerung § 6 AStG:** Wer mit ≥ 1 % an einer deutschen GmbH
    beteiligt ist und wegzieht, muss auf stille Reserven ggf. Steuern
    zahlen – bei einer Firma mit Wert (Marke, Kundenstamm) ein echtes Thema.
  - **§ 2 AStG (erweiterte beschränkte Steuerpflicht):** deutsche
    Staatsangehörige bleiben nach Wegzug bis zu 10 Jahre für bestimmte
    inländische Einkünfte und Situationen an Deutschland angebunden.
- **Türkei-Risiken bleiben:** zweistellige Inflation, TRY-Abwertung,
  Rechtsdurchsetzung; Verträge in EUR, kurze Zahlungsziele (Kap. 10).
- **Fördernachteil:** KfW/BAFA/ZIM/Forschungszulage gibt es nur für deutsche
  Betriebsstätten/Gesellschaften – ein früher Wegzug verzichtet auf genau die
  Zuschüsse, die in P1–P3 mehr wert sind als jede Steuerersparnis (in der
  Anfangsphase sind Verluste zu erwarten; Steuern fallen auf Verluste keine an).

### 8.3 Praktische Strategie für SunWall (Staffelplan)

| Zeitraum | Schritt | Begründung |
|---|---|---|
| **Jahr 0–2 (P1–P3)** | Gründung in **Deutschland**; Fördermittel nutzen (Kap. 7); Struktur „wegzugsfähig" halten: keine überflüssigen stillen Reserven, IP-Dokumentation sauber getrennt | Zuschüsse + Marktzugang EU + einfache Buchhaltung schlagen Steuerersparnis auf Verlustebene |
| **Jahr 2–3 (P4)** | Wenn das türkische Programm **Gesetz ist und die Details klar**: prüfen, eine **Sales-/Holding-Gesellschaft in der Türkei** (Regional-HQ-Regime) zu platzieren und die Serienfertigung der Blechteile dorthin zu verlagern (ohnehin geplant, Kap. 4.3) | Hier greifen die Befreiungen tatsächlich: HQ-/Vertriebsfunktion + Export |
| **Weiterhin** | Deutsche GmbH bleibt als **Lager-/Service-Betriebsstätte** für EU-Kunden (schnelle Lieferung, Gewährleistung) | EU-Marktzugang, aber: Gewinne dieser DE-Betriebsstätte bleiben DE-steuerpflichtig |
| **Vor jedem Schritt** | Deutsch-türkischer Steuerberater: Wegzugsbesteuerung, DBA, § 2 AStG, Betriebsstätten-Fiktionsprüfung; Kosten der Umsetzung (Beratung, Umzug, Buchhaltung zweiländig) gegen die reale Ersparnis rechnen | Bei Kleinserie ist die Ersparnis oft kleiner als der Aufwand |

**Faustregel:** „Steuerparadies" ist die Türkei für dieses Projekt erst ab dem
Punkt, an dem **Gewinne** anfallen (P4/P5) – und selbst dann nur für die
Teile des Geschäfts, die die Befreiungen wirklich abdecken. Die Anfangsphase
gewinnt deutlich mehr durch deutsche Fördermittel als durch Steuervermeidung.

### 8.4 Offene Punkte (beobachten)

- [ ] Gesetzgebung zum Strong Investment Hub Program verfolgen (Umsetzung der
      angekündigten 9 % Exporteure-KSt, Regional-HQ-Bedingungen, Schwellen)
- [ ] Kriterien des Regional-HQ-Regimes: Mindestbeschäftigung, Mindestumsatz,
      Tätigkeitsanforderungen – entscheiden über Machbarkeit für ein
      Kleinstunternehmen
- [ ] Erstgespräch mit deutsch-türkischer Steuerkanzlei sobald P4 näher rückt

## 9. IP- und Markenschutz

- **Marke:** „SunWall“ und „Netzfrei“ früh als Wortmarke beim **DPMA**
  (Deutschland, ~290 € je Klasse) bzw. **EUIPO** (EU, ~850 €) sichern –
  vor dem ersten öffentlichen Auftritt des Produkts.
- **Konstruktion:** Fertigungszeichnungen/BOM nur nach NDA an Dienstleister;
  Werkzeuge und Programmdateien (DXF, NC) vertraglich in unser Eigentum.
- **Open-Hardware-Spannung:** Bauanleitungen und Messdaten bleiben offen
  (Vertrauen + SEO, siehe `13-produkt-sunwall.md`), aber **Fertigungs-
  optimierte Zeichnungen, Firmware-Release-Konfiguration und Lieferanten-
  konditionen** bleiben geschlossen. Die Marke ist der Schutz, nicht das
  Geheimnis: copied wird ohnehin – der Vorsprung ist Marke + Qualität +
  Netzfrei-Integration + Preis.
- **Verträge mit Fertigern:** schriftlich, mit Geheimhaltungs-, Werkzeug-,
  Ausschuss- und Gewährleistungsregelung; kein Exklusivrecht ohne Kompensation.

## 10. Risiken und Grenzen

- **Türkei-Steuerprogramm:** die 20-Jahres-Befreiungen sind teils noch
  Gesetzesvorlage und decken nicht das ganze Geschäft ab (siehe Kap. 8) –
  keine Struktur-Entscheidung auf Basis von Schlagzeilen.
- **Preisangaben sind Erfahrungswerte, keine Angebote** – alles muss per RFQ
  (Kap. 6) verifiziert werden; Blech- und Elektronikpreise schwanken deutlich
  (Alu/Stahl-Börsen, Halbleiter-Zyklen).
- **Türkei:** Währungs- und Länderrisiko (TRY-Inflation, politische Lage) –
  Verträge in EUR, kurze Zahlungsziele, Zweitquelle in der EU parallel halten.
- **A.TR/Zollunion:** funktioniert für Industriegüter reibungslos, aber
  Dokumentationsfehler kosten Zeit; für Stahlwaren (Kapitel 72) Ausnahmen
  prüfen – ggf. Alu statt Stahl wählen.
- **Kleinserien-Qualität:** ohne eigene Endkontrolle verliert das Produkt
  sein Qualitätsversprechen – der Prüfstand aus P1 bleibt auch in Serie die
  Stichproben-Instanz (z. B. 1 von 20 Modulen voll gemessen).
- **Fördermittel sind zweckgebunden** und erfordern Verwendungsnachweise;
  keine Zusagen vor Antrag. Programme ändern sich jährlich – Stand prüfen.

## 11. Nächste Schritte

- [ ] Türkisches Investitionsprogramm (Strong Investment Hub) beobachten;
      Sitz-Strategie erst bei Gesetzestext + Beratergespräch festlegen (Kap. 8)
- [ ] NDA-Vorlage + RFI an 5–8 Blechzentren (DE/PL/TR) senden, Angebote einholen
- [ ] Ventilator-RFQ: EU-Großhandel vs. Direktimport (MoQ, Muster) vergleichen
- [ ] Prüfstand (P1) als Forschungszulage-Projekt skizzieren (Steuerberater/FZulG)
- [ ] Markenrecherche „SunWall“/„Netzfrei“ (DPMA/EUIPO) + Anmeldung nach P2
- [ ] Werkstatt-Ausstattungsliste für Stufe A/B (Kap. 2) aufstellen
- [ ] Nach RFQ-Ergebnissen: Kostenkalkulation in `04-kosten-roadmap.md` Phase 5 aktualisieren
