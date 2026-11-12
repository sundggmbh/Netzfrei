# 03 – Netzfrei: Lokale KI als Energieleitsystem (EMS)

**Netzfrei** ist der Name des lokalen KI-Heimnetzwerks von AUTARQ: die Software
und das Netzwerk, die alle Komponenten des Gebäudes messen, steuern und
optimieren – lokal, ohne Cloud-Zwang.

## 1. Prinzip: Ein Haus, eine KI, kein Cloud-Zwang

Netzfrei läuft **lokal im Gebäude** (auf dem Homelab-Server selbst – dessen
Abwärme heizt ja ohnehin mit). Es trifft Entscheidungen in 1-Minuten-Takten und
funktioniert auch ohne Internet; dynamische Strompreise und Wetterprognosen sind
Optionen, keine Voraussetzung.

## 2. Entscheidungslogik

Das EMS kennt pro Zeitpunkt:

- **Erzeugung:** PV-Leistung (aktuell + 24-h-Prognose aus lokalem Wettermodell),
- **Preis:** dynamischer Tarif (z. B. Viertelstundenpreise) oder feste Zeitfenster
  („abends teuer, nachts günstig") – konfigurierbar, auch komplett netzunabhängig,
- **Bedarf:** Raumtemperaturen, Warmwasservorrat, Batteriestand, erwartete Bewohner-
  aktivität (lernend aus Gewohnheiten),
- **Lasten:** verlagerbar (WP, Server, Waschmaschine, E-Auto) vs. fix (Licht, Kochen).

### Priorisierung (vereinfachte Zielfunktion)

1. **Eigenverbrauch maximieren:** PV-Überschuss zuerst in Batterie, dann thermisch
   in den Pufferspeicher (Warmwasser/Heizung auf Vorrat), dann in verlagerbare Lasten.
2. **Kosten minimieren:** Bei dynamischem Preis wird verlagert – Waschmaschine,
   Ladung, Serverlast und WP-Verdichter laufen nachts/günstig, der Pufferspeicher
   trägt die teuren Abendstunden thermisch über.
3. **Autarkie priorisieren:** Im Inselbetrieb (netzunabhängig) gilt statt des Preises
   der Batteriestand – die KI drosselt dann Komfortlasten (Licht-Szenen, Serverlast)
   bevor kritische Lasten (Kühlschrank, WP) leiden.
4. **Komfort-Grenzen:** Temperaturbänder pro Raum (z. B. 21 ± 1 °C), Tauwacht im
   Kühlbetrieb, Legionellenschutz für Warmwasser – nicht verhandelbar.

## 3. Beispiel: ein typischer Wintertag (gemäßigtes Klima)

| Uhrzeit | Situation | KI-Entscheidung |
|---|---|---|
| 00–05 h | Netzstrom günstig, PV 0 | Pufferspeicher auf 45 °C laden, Batterie voll, Server Volllast |
| 05–08 h | Bewohner aufstehen | Warmwasser aus Puffer, Heizung aus Puffer – kein Verdichter |
| 08–16 h | Sonne | PV deckt Haushalt, Überschuss → Puffer (thermisch) + Batterie |
| 16–21 h | Netzstrom teuer | Alles aus Batterie + Puffer; WP aus, Server gedrosselt |
| 21–24 h | Preis sinkt | Batterie nachladen, ggf. WP-Nachlauf |

## 4. Software-Architektur von Netzfrei

```
┌─────────────────────────────────────────────────┐
│              HOMELAB-SERVER (lokal)             │
│                                                 │
│  ┌────────────┐   ┌───────────────────────┐    │
│  │ Home       │◄──┤  KI-Ebene (lokal):    │    │
│  │ Assistant  │   │  Zeitreihen-Prognose  │    │
│  │ (Bus,      │   │  (PV, Bedarf, Preis)  │    │
│  │  Sensoren, │   │  Optimierer (MPC oder │    │
│  │  Aktoren)  │   │  Regelbasiert + LLM-  │    │
│  └────────────┘   │  Assistent für Nutzer)│    │
│        ▲          └───────────────────────┘    │
│        │                                        │
│  Modbus/KNX/Thread: WP, Batterie, Zähler,      │
│  Ventile, Pumpen, Licht, Steckdosen            │
└─────────────────────────────────────────────────┘
```

- **Untere Ebene:** Home Assistant (open source) als Bussystem-Abstraktion –
  unterstützt Modbus, KNX, Zigbee, Thread, MQTT out-of-the-box. Systemvergleich,
  Funk-Standards und Einkaufsliste: `10-smart-home-systeme.md`.
- **Optimierung:** model-predictive control (MPC) über 24 h Horizont; Start als
  einfache Regelbasierte Logik, Ausbau zu gelernten Prognosen.
- **Assistent:** lokales Sprach-/Chat-LLM (z. B. auf dem Homelab) für Bedienung
  auf Deutsch/Englisch: „Heize das Bad ab 17 Uhr vor, aber nur mit PV."
- **Sicherheit:** Alle Regelungen haben hardwareseitige Grenzen (Therme-Logik in
  der WP selbst), die KI darf nur innerhalb sicherer Bänder steuern.

## 5. Netzwerk (ein Haus, ein Netzfrei)

- **Kabelgebunden:** Powerline-Ethernet oder CAT-Verkabelung im Neubau für WP,
  Batterie, Zähler, Server – kritische Infrastruktur ohne Funk.
- **Funk:** Thread/Zigbee-Mesh für Sensoren, Licht, Steckdosen ( batteriebetrieben,
  niedrigster Energieverbrauch).
- **Ausfallsicherheit:** Netzfrei läuft auf dem Homelab; fällt es aus, übernehmen
  lokale Fallback-Regler (WP-Controller, Thermostatventile) den Grundbetrieb.

## 6. Netzfrei als Produkt

Netzfrei ist mehr als Steuerung – es ist das verkaufbare Software-Produkt des
Projekts:

- **Ein Image, ein Gerät:** Netzfrei als bootbares System-Image (auf dem Homelab
  oder einem 50-€-Mini-PC) – flashen, Sensoren koppeln, fertig.
- **Offen:** Open Source (Apache-2.0), jede Gemeinde/jeder Selbstbauer kann es
  anpassen.
- **Markenname:** „AUTARQ powered by Netzfrei“ – das Haus ist die Hardware,
  Netzfrei ist das Gehirn.

## Ergänzung: EMS v1 als Code

Die regelbasierte EMS-Logik (Priorisierung Eigenverbrauch → Kosten →
Autarkie → Komfort) ist als ausführbarer Code umgesetzt:
`software/netzfrei/ems.py` mit Unit-Tests (`software/tests/`) und
Wintertag-Simulation (`software/simulation.py`). Architektur/Setup:
`software/README.md`.
