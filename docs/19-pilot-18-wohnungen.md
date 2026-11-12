# 19 – Pilotobjekt: 18 Wohnungen sanieren (Demo-Objekt der GmbH)

Ausgangslage: Die GmbH hat **18 Wohnungen** zu sanieren. Plan aus der Diskussion:
diese Sanierung mit dem AUTARQ-System (SunWall, Klimageräte-Umbau, KWL, Heizfolien,
Netzfrei) durchführen – als **Pilot-/Demo-Objekte**. Damit wird die eigene Sanierung
zum Testfeld, Messdaten-Lieferanten und stärksten Verkaufsargument.

**Standort: [ORT_NACHTRAGEN]** (bitte nachliefern – relevant für Klima, Einstrahlung,
Landesförderung, Denkmalschutz). Gebäudeart: [MFH/EFH-Gruppe], Baujahr: [XX],
Heizung heute: [XX].

---

## 1. Warum 18 Wohnungen ideal sind

1. **Mehrfamilienhaus-Förderstufen:** Die BEG fördert je Wohneinheit gestaffelt
   (Kap. 2) – 18 WE sind ein großer Fördertopf.
2. **Echtes Testfeld mit Stufen:** 2 Pilot-WE → Auswertung → Rollout. Fehler kosten
   2 WE, nicht 18.
3. **Referenzobjekt:** Messdaten aus 18 realen Wohnungen (3 Heizperioden) sind das
   stärkste Verkaufsargument überhaupt – „bei uns läuft es, hier sind die Zahlen".
4. **Netzfrei-Skalierungstest:** Ein Gebäude mit 18 WE ist genau der Fall, für den
   das KI-Agentennetzwerk gebaut wird (Kap. 5).
5. **GmbH als Eigentümer:** Ein Antragsteller, ein Ansprechpartner, volle Kontrolle
   über den Zeitplan – kein Mieter-Vermieter-Knoten bei der Antragstellung
   (Mieter-Beteiligung trotzdem beachten, Kap. 3).

---

## 2. Förderrechnung (BEG MFH, Stand 2025/2026, ohne Gewähr)

| Wohneinheit | Förderfähige Kosten (ab 21.07.2026) | Anzahl | Summe |
|---|---|---|---|
| 1. WE | 28.000 € | 1 | 28.000 € |
| 2.–6. WE | 15.000 € | 5 | 75.000 € |
| ab 7. WE | 8.000 € | 12 | 96.000 € |
| **Gesamt förderfähig** | | **18** | **199.000 €** |

**Fördersätze für die GmbH (Vermieter):** Grundförderung 30 % +
Klimageschwindigkeitsbonus +16 % (Austausch fossiler/alter Heizung vor Ende 2028;
Treppe: −4 % je Halbjahr ab Feb 2027, entfällt Aug 2028) = **46 %** im besten Fall.
Der Einkommensbonus (bis 80 %) gilt für Selbstnutzer – bei Vermietung in der Regel
nicht anwendbar. 

**Realistische Fördersumme: 46 % von 199.000 € ≈ 91.500 €** – bei umfassendem
Austausch (WP + Warmwasser + Anlagenanschluss + Demontage). Wichtig:

- **Antrag vor Vorhabenbeginn** (Vertragsabschluss!) – bei 18 WE ggf. gestaffelte
  Anträge je Baublock, aber vor jedem einzelnen Vertrag.
- **Kombinationsverbot** BEG EM ↔ BEG WG beachten: Entweder Einzelmaßnahmen
  (Heizung + KWL je förderfähig) oder Komplettsanierung zum Effizienzhaus
  (Tilgungszuschuss bis ~45 %) – mit Energie-Effizienz-Experten (EEE) vor
  Antragstellung durchrechnen. Bei 18 WE lohnt der EEE in jedem Fall.
- Steuerbonus § 35c EStG als Alternative für nicht-BEG-fähige Positionen prüfen
  (Handwerkeranteil; schließt BEG für dieselbe Maßnahme aus).
- **SunWall:** nicht BEG-förderfähig (doc 16 Kap. 4.1) – läuft über die
  Investitionsrechnung (Erntefaktor 20–80) und als Demo-Anlage, nicht über Förderung.
- Heizfolien/-farbe: nicht förderfähig – als gezielte Ergänzung (Bad, kalte Ecke)
  aus Eigenmitteln, bewusst klein kalkuliert (doc 05/07).

---

## 3. Mieter & Recht (wenn vermietet)

- **Modernisierungsankündigung** (§ 554 BGB): Maßnahmen mit Frist von 3 Monaten
  ankündigen; Ausnahme-Härten prüfen.
- **Mieterhöhung** (§ 559 BGB): 8 % der Modernisierungskosten auf die Jahresmiete
  pro Modernisierungsumfang – bei Förderung zählen die **geförderten** Kosten
  (Netto-Investition) → Förderung senkt die zulässige Erhöhung, fair und
  konfliktarm kommunizieren.
- **Zutritt/Zeitplan:** Klimageräte-Außengeräte + SunWall = wenig Aufwand in den
  Wohnungen (1–2 Tage je WE); KWL = Kanalnetz, der größte Eingriff → in der
  Pilot-Phase testen, ob Mieter-Koordination tragbar ist.
- **Eigennutzung?** Falls (Teil der) 18 WE eigengenutzt: diese WE zuerst sanieren –
  dort gilt der volle Förderdeckel bis 70/80 %.

---

## 4. Sanierungs-Paket je Wohneinheit (Stufen)

| Stufe | Maßnahme | Kosten je WE (grob) | Förderfähig | Doc |
|---|---|---|---|---|
| **P1** | Klimagerät mit Heizfunktion (Luft-Luft-WP, A++, Smart-Grid, R290) inkl. Fachmontage | 900–1.800 € | **JA** (KfW 458, 46 %) | `11-klimageraete-umbau.md` |
| **P2** | Warmwasser-Modul (Luft-Wasser-Umbau) wo sinnvoll | 1.500–3.000 € | **JA** | `11` Pfade B/C |
| **P3** | SunWall-Modul an der Süd-Fassade (je WE-Fenster) | 250–450 € | nein (Demo-Wert) | `12`/`13` |
| **P4** | KWL mit WRG (nur Pilot-WE zuerst) | 2.000–4.000 € | **JA** (BAFA ~15 %) | `06` |
| **P5** | Heizfolie/-farbe als Ergänzung (Bad, kalte Ecke) | 100–400 € | nein | `05`/`07` |
| **P6** | Netzfrei-Knoten (Messung + EMS, Hausbus) | 150–300 € | teils (smarte Technik) | `software/` |

**Gebäudeebene (einmalig):** PV-Anlage (Dach) + Batterie + SunWall-Wand an der
Südfassade + zentrale Netzfrei-Zentrale. PV/Batterie über KfW 270 (Kredit) bzw.
EEG (Eigenverbrauch) wirtschaften, nicht über BEG.

**Beispielrechnung Pilot-WE (P1 + P3 + P6):** ~1.300–2.550 € Investition, davon
~46 % auf P1 gefördert → Netto ~1.000–1.900 € je WE. Erst messen, dann Rollout.

---

## 5. KI-Agentennetzwerk (Netzfrei) im Gebäude

Die 18 WE sind der Skalierungstest für die Netzfrei-Architektur
(`software/README.md`, `software/netzfrei/ems.py`). Rollenbild:

| Agent | Aufgabe | Basis heute |
|---|---|---|
| **WE-EMS-Agent** (×18) | Je Wohnung: Überschuss-Nutzung, Komfort-Band, Temperatur-Soll | `ems.py` `entscheide()` – bereits getestet |
| **Gebäude-Agent** | Lastmanagement: 18 × 5 kW WP = 90 kW Spitze → Staffelbetrieb, Priorisierung, Netzanschluss-Grenze einhalten | neu (Phase 2) |
| **PV-/Prognose-Agent** | Erzeugungs- und Wetterprognose (SunWall + PV), Preisfenster | Simulation-Logik vorhanden |
| **Mess-/Doku-Agent** | Messdaten sammeln, QC-Protokolle, Förder-Nachweise, Case-Study-Daten | neu (Phase 2) |
| **Wartungs-Agent** | Filterstände, Ventilator-Laufzeit, Fehlercodes → Wartungsplan | neu (Phase 3) |

**Wichtige Ingenieur-Aufgabe zuerst:** Netzanschluss prüfen. 90 kW WP-Spitze
gleichzeitig ist realistisch zu verhindern durch: Staffelbetrieb (Gebäude-Agent),
Sonnen-/Kollektor-Vorheizung (SunWall senkt WP-Laufzeit), Warmwasser-Zeitfenster.
Das ist genau die Demonstration, die Netzfrei als Produkt beweisen muss.

**Stufen:** Phase 1 = regelbasiert (heutiger Code, 2 Pilot-WE) → Phase 2 =
Gebäude-Agent + Mess-Agent (Rollout) → Phase 3 = MPC/Prognose (alle 18 WE).

---

## 6. Zeitplan (ankoppeln an den Dezember-Launch, doc 18)

| Monat | Schritt |
|---|---|
| **M1** | Bestandsaufnahme: Heizlast je WE, Netzanschluss, Dach/Fassade (Süd-Fläche für SunWall), Denkmalschutz? EEE beauftragen |
| **M1–M2** | BEG-Antrag(en) stellen (VOR Verträgen!); KfW-458-Konditionen tagesaktuell prüfen |
| **M2–M3** | **Pilot: 2 WE** komplett (P1+P3+P5+P6), SunWall-Fassade 1. Abschnitt, Messaufbau |
| **M4** | Auswertung Pilot: Ertrag, ΔT, Komfort, Mieter-Feedback, Kosten real vs. Plan |
| **M5–M9** | Rollout in Tranchen (je 4–6 WE), Gebäude-Agent live, Lastmanagement in Betrieb |
| **M10–M12** | KWL-Pilot auswerten, Case-Study schreiben, Messdaten veröffentlichen (Track D, doc 18) |
| **ab M12** | **Demo-Objekt in Vermarktung:** Besichtigungen für Interessenten & Partner, Messdaten-Widget auf der Webseite, Video-Tour |

---

## 7. Demo-Objekt als Verkaufsargument (Verwertung)

1. **Case-Study-Seite** auf der Webseite: „18 Wohnungen, echte Zahlen" – Ertrag,
   Einsparung, Förderquote, Zufriedenheit.
2. **Besichtigungstermine** für Wartelisten-Kunden und SHK-Partner (Vertrauen vor
   Kauf).
3. **Messdaten open:** wie die Bauanleitung – Transparenz als USP (doc 13 Kap. 6).
4. **Referenz für B2B:** Wohnungsbaugesellschaften, Gewerbe (SW-Pro), Agrar –
   „Referenzobjekt saniert" öffnet genau diese Türen.
5. **Förder-Dokumentation als Vorlage:** Der komplette Antrags- und Nachweis-Weg
   wird dokumentiert und wird Muster für den Förder-Check-Service (doc 16 Kap. 6).

---

## 8. Risiken

- **BEG-Treppe:** Klimageschwindigkeitsbonus sinkt (16 % → 0 % bis Aug 2028) –
  Antrag so früh wie möglich, Förderquote im Businessplan mit 30 % Grundförderung
  kalkulieren (Bonus = Upside, nicht Planbasis).
- **Denkmalschutz / Fassade:** SunWall + Außengeräte brauchen ggf. Genehmigung –
  in M1 klären.
- **Mieter-Widerstand:** früh kommunizieren, Förderersparnis transparent machen
  (Kap. 3), Pilot-WE als Aushängeschild nutzen.
- **Kapazität:** 18 WE parallel mit Lohnfertigungs-Start (doc 18) kollidiert –
  deshalb Tranchen (M5–M9), Pilot zuerst.
- **Kostenrealität:** Grob-Kosten hier sind Planwerte; nach Pilot-WE (M4) neu
  kalkulieren, bevor der Rollout freigegeben wird.

---

## 9. Nächste Schritte

1. Standort/Gebäudedaten nachliefern (Ort, Baujahr, Heizung, Dach-/Fassadenfläche,
   Netzanschluss) → Bestandsaufnahme M1 starten.
2. EEE beauftragen: BEG EM vs. BEG WG für 18 WE durchrechnen (Kombinationsverbot!).
3. Pilot-WE auswählen (Süd-Fassade, kooperative Mieter bzw. Eigennutzung).
4. Netzanschluss-Potenzial beim Netzbetreiber anfragen (90-kW-Frage, Kap. 5).
5. Sanierungs- und Launch-Kalender zusammenführen (doc 18): Prototyp-/Charge-1-
   Material fließt zuerst in die Pilot-WE – das Objekt ist der erste Kund.
