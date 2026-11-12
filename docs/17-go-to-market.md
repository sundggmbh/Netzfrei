# 17 – Go-to-Market: SunWall verkaufsfertig machen (parallel, ohne Warten)

Ziel aus der Diskussion: Das Produkt so weit fertig machen, dass **jetzt** eine
Webseite live gehen und verkauft werden kann – während Prototyp, Fertigungsarchitektur
und Netzfrei-Software **gleichzeitig** weiterlaufen. Nichts soll auf nichts warten.

**Firmenmotto als Verkaufsversprechen:** *Einfach, kostengünstig, unabhängig –
für jeden bezahlbar.*

---

## 1. Was ist ab Tag 1 verkaufbar? (MVP-Produkt)

**Verkauft wird der Bausatz, nicht das zertifizierte Fertigsystem.** Das ist der
entscheidende Trick: Ein Bausatz (Lochblech + Dämmung + Kasten + Ventilator-Set +
Anleitung) braucht keine Heizungs-Zertifizierung, keine Wärmeerzeuger-Liste, kein
Solar-Keymark – und kann mit Lohnfertigung (doc 14) sofort in Kleinserie gebaut werden.

| MVP | Inhalt | Preis (doc 13) | Status |
|---|---|---|---|
| **SW-1.0 Starterkit** (1 m²) | Lochblech, Kasten, 12-V-Ventilator-Set, Montage-Winkel, Bauanleitung | 149–199 € | **ab Tag 1 verkaufbar** |
| **SW-2.0 Bausatz SW-U** (2 m², unglazed) | + gedämmtes Plenum (110 mm), PWM-Regelung | 249–349 € | **ab Tag 1 verkaufbar** |
| **SW-2.0 Bausatz SW-G** | + 4-mm-Glas, 30 mm Abstand | 349–449 € | ab Lohnfertigung (Glaszuschnitt) |
| **SW-Solar-Option** | PV-Direkt-Ventilator-Set, komplett autark | +20–40 € | **ab Tag 1** |
| **Mess-Kit** | 2× T-Sensor, Anemometer-Einschub, Log-Auswertung | ~50 € | Phase 2 (nach Prüfstand) |

**Kernversprechen auf der Webseite (alle Zahlen aus docs 12/13, ehrlich gerahmt):**

- ΔT bis 40 K bei klarem Winterlicht, 400–800 W je 2-m²-Modul (SW-G)
- Jahresertrag 400–700 kWh pro Modul (Mitteleuropa, Südfassade)
- Erntefaktor 20–80 kWh Wärme pro kWh Strom (12-V-Ventilator); SW-Solar: null
  Netzstrom
- Material ~30–80 €/m² – wir verkaufen das geprüfte, dokumentierte Bausatz-System
  im DIY-Preisband
- **Ehrlichkeit als Feature:** jede Angabe mit Messprotokoll-Referenz, Grenzen
  (Wind, Bewölkung, Ost/West-Fassade) stehen im FAQ – das ist der USP gegen
  Fernost-Importe und gegen Overclaiming

**Was bewusst NICHT versprochen wird (bis Phase 2/3):** Solar-Keymark, Förderfähigkeit
über BEG, Netzfrei-Fertigintegration (liegt als „beta, open source" bei), Warmwasser.

---

## 2. Vier parallele Tracks (nichts wartet auf nichts)

```
Track A: PRODUKT/FERTIGUNG      Track B: WEB/SHOP
  Prototyp + Pruefstand           Webseite live (heute: statisch)
  Lohnfertigung-RFIs (doc 14)     Bestellungen via E-Mail/Warteliste
  QC-Messprotokolle               Shop-Backend spaeter
        |                               |
        +------------+------------------+
                     |
Track C: PARTNER/FOERDER-CHECK   Track D: CONTENT/MARKETING
  3 SHK-Betriebe ansprechen       Bauanleitung offen (GitHub)
  EEE-Kontakte (doc 16)           YouTube-Bautagebuch
  Fachbetrieb-Qualifizierung      SEO-Artikel, Messdaten-Publikation
```

**Regel: Jeder Track hat ein Deliverable, das ohne die anderen Track-Ergebnisse
funktioniert.** Der Shop verkauft ab Tag 1 mit Warteliste, auch wenn der Prototyp
noch misst; die Messdaten aus Track A füttern Track D; Track C braucht nur die
Produktspezifikation, nicht die Serie.

| Track | Diese Woche | Dieser Monat | Quelle |
|---|---|---|---|
| **A Produkt** | Prototyp-BOM bestellen, Prüfstand-Teileliste | Erste Messkennlinie, Lohnfertigung-RFI an 3 Blechzentren | `12-sonnenluftkollektor.md`, `14-produktion-auftragsfertigung.md` |
| **B Web** | **Webseite live** (dieses Repo, `website/`), Domain, E-Mail | Bestellablauf (Rechnung/Vorkasse), erste Warteliste anschreiben | `website/README.md` |
| **C Partner** | 3 SHK-Betriebe + 1 EEE anschreiben (RFI-Vorlage) | Förder-Check-Formular verfeinern, Partner-Seite mit Logo | `16-foerdermittel-endkunden.md` |
| **D Content** | ~~Bauanleitung v1~~ erledigt (`website/bauanleitung.html`), 3 SEO-Artikel | Bautagebuch-Video 1, Messdaten-Widget auf Startseite | `13-produkt-sunwall.md` Kap. 6 |

---

## 3. Launch-Phasen

1. **Pre-Launch (ab sofort):** Webseite mit Warteliste („Erste Charge: 50 Module,
   Lieferung ~6 Wochen"). Warteliste validiert Preis und Nachfrage **bevor** die
   Lohnfertigung beauftragt wird – Null-Risiko-Start.
2. **Soft-Launch (Charge 1):** 20–50 Bausätze SW-1.0/SW-U an die Warteliste, jeder
   Kunde bekommt das Mess-Protokoll-Formular → Rücklauf = Testimonials + Messdaten
   für Track D.
3. **Skalierung:** ab ~500 Modulen/Jahr eigene Fertigung (doc 14), SW-G, SW-Wand,
   B2B (Agrar-Trocknung), Netzfrei-Bundle.
4. **Türkei (Jahr 2–3):** TR-Markt + Fertigung parallel (doc 14 Kap. 4.4/8).

---

## 4. Rechtliches Minimum (vor dem ersten Verkauf)

- **Impressum + Datenschutz:** Pflicht (TMG/DDG, DSGVO) – Platzhalter in
  `website/impressum.html` / `website/datenschutz.html`, **vor Launch ausfüllen**
  (Firmenanschrift, Vertretung, Host-/Shop-Datenverarbeitung).
- **Fernabsatz:** Widerrufsbelehrung (14 Tage) + AGB auf der Bestellseite; bei
  individualisierten Bausätzen kein Ausschluss nötig, Standardware = Widerrufsrecht.
- **Produktsicherheit:** Das 12-V-Ventilator-Set ist ein elektrisches Produkt →
  CE-Konformität des Ventilators vom Lieferanten fordern (RoHS/EMV-Lieferschein).
  Der Bausatz ohne Spannungsquelle > 12/24 V DC hält den regulatorischen Aufwand
  klein; **keine 230-V-Komponenten im MVP**.
- **Gewährleistung:** 2 Jahre gesetzlich; Ventilator als Verschleißteil offen
  kommunizieren (Ersatzteil-Preisliste = Vertrauen + Folgeumsatz).
- **Markenschutz:** „SunWall" + „Netzfrei" DPMA/EUIPO-Anmeldung **vor** dem
  Launch-Kanal-Aufbau (doc 14 Kap. Marken-Anmeldung).
- **Keine Steuer-/Rechtsberatung im Förder-Check** – Formular liefert nur eine
  Erst-Einschätzung „ohne Gewähr" (doc 16 Kap. 6).

---

## 5. Risiken & Grenzen

- **Overclaiming-Gefahr:** Alle Leistungszahlen stammen aus Forschung + eigener
  Prototyp-Zielsetzung; bis Charge 1 mit eigenen Messungen belegen, sonst
  „Zielwerte" labeln.
- **Ein-Personen-Last:** 4 Tracks sind viel – Reihenfolge in Track B/D automatisieren
  (statische Seite, mailto-Bestellung) statt Shop-Backend zu früh zu bauen.
- **Preisdruck Fernost:** Nicht über Preis allein kämpfen – Doku, Messdaten und
  Support sind die Verteidigung (doc 13 Kap. 2).
- **Förder-Erwartung:** Kunden dürfen nicht „70 % Zuschuss auf SunWall" erwarten –
  FAQ stellt das klar (doc 16 Kap. 4.1).

---

## 6. Nächste Schritte

Der konkrete Wochen-Countdown bis zum Dezember-Launch (Inserate, Broschüre,
Warteliste live) steht in `18-dezember-launch.md`; fertige Anzeigentexte in
`marketing/anzeigen-texte.md`, die Druck-Broschüre in `website/broschuere.html`.

1. Webseite-Review + Domain + Impressum-Daten → Pre-Launch.
2. Wartelisten-Text scharf stellen (Charge-1-Limit „50 Module" ehrlich an
   Lohnfertigungs-Kapazität koppeln).
3. Prototyp-BOM bestellen (Track A Start), Prüfstand nach doc 13 Kap. 5.
4. RFI an 3 Blechzentren (doc 14 Vorlage) mit Charge-1-Stückzahl 50.
5. DPMA-Voranfrage „SunWall"/„Netzfrei" (Klassen 11, 9, 35).
