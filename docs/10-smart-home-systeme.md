# 10 – Smart-Home-Systeme: Auswahl für Netzfrei

## 1. Anforderung an das Smart-Home-System in AUTARQ

| Anforderung | Warum |
|---|---|
| **Lokal lauffähig (kein Cloud-Zwang)** | Netzfrei-Prinzip: funktioniert ohne Internet, keine Datenabflüsse |
| **Modbus/KNX-Anbindung** | Wärmepumpe, Batterie, Wechselrichter, Zähler sprechen Modbus; Gebäudeinstallation ggf. KNX |
| **Mesh-Funk für Sensoren** | Zigbee/Thread für batteriebetriebene Temperatur-/Anwesenheitssensoren |
| **Open Source / offene Standards** | Für immer wartbar, keine Herstellerabhängigkeit, Selbstbauer-freundlich |
| **Automatisierungs-Engine + API** | MPC-Optimierer und LLM-Assistent müssen direkt eingreifen können |
| **Kosten** | Software gratis, Hardware aus dem Billigsegment (Shelly, Zigbee-No-Name) |

## 2. Systemvergleich

| System | Lizenz | Lokal? | Stärken | Schwächen | Urteil |
|---|---|---|---|---|---|
| **Home Assistant** | Open Source (Apache-2.0) | Ja (100 %) | Größte Geräteunterstützung (>2.500 Integrationen), Modbus/KNX/Zigbee/Thread/Matter nativ, Python-API, riesige Community, Add-on-System | Einarbeitung nötig | **Wahl für Netzfrei** |
| openHAB | Open Source | Ja | Sehr stabil, Java, gute Bindings | Ältere UX, kleinere Community | Alternative |
| ioBroker | Open Source | Ja | Stark im deutschsprachigen Raum | Kleineres Ökosystem international | Alternative |
| Loxone | Proprietär | Teils | Komplett-System für Neubau | Hersteller-Lock-in, teuer (Config-Software, Lizenz), kein offener Standard | Nein |
| KNX | Offener Standard (zertifiziert) | Ja | Industriestandard für Gebäudeinstallation, extrem robust, Kabelgebunden | Teure Komponenten (30–80 €/Aktor), Zertifizierung nötig | Nur für Kern-Installation im Neubau (optional) |
| Tado/Nest/SmartThings | Proprietär | Nein (Cloud) | Einfach | Cloud-Abhängigkeit widerspricht Autarkie | Nein |

## 3. Funk- und Bus-Standards

| Standard | Frequenz/Topologie | Einsatz in AUTARQ | Kosten/Aktor |
|---|---|---|---|
| **Zigbee 3.0** | 2,4-GHz-Mesh | Sensoren (Temperatur, Feuchte, CO₂, Anwesenheit), Lampen, Steckdosen | 8–25 € |
| **Thread/Matter** | 2,4-GHz-Mesh, IP-basiert | Zukunftsstandard, interoperabel – bevorzugt für Neukauf | 10–30 € |
| **Modbus RTU/TCP** | Kabel (RS-485/Ethernet) | WP, Batterie, Wechselrichter, Energiezähler, Netzfrei↔Geräte | Kabel + 10–30 €/Zähler |
| **KNX** | Kabelbus (Twisted Pair) | Neubau-Kerninstallation (Licht, Ventile, Rollo) – optional | 30–80 €/Aktor |
| Wi-Fi | – | Nur für Kamera/Unterhaltung, nicht für Regelung (zu stromhungrig, instabil) | – |

**Prinzip: Kabel für alles, was Geld kostet oder sicher sein muss (WP, Batterie,
Zähler, Heizventile); Funk nur für Sensoren und Licht.**

## 4. Konkrete Einkaufsliste (120-m²-Referenz, DIY-Preise)

| Komponente | Anzahl | Stückpreis | Summe |
|---|---|---|---|
| Homelab/Mini-PC (Netzfrei-Host, N100-Klasse) | 1 | 150–250 € | 200 € |
| Zigbee/Thread-Coordinator (USB-Stick) | 1 | 25–40 € | 30 € |
| Energiezähler Modbus (PV, Batterie, WP, Haus) | 4 | 30–60 € | 180 € |
| Temperatur-/Feuchtesensoren Zigbee | 10 | 8–15 € | 120 € |
| Anwesenheitssensoren (mmWave/PIR) | 5 | 15–30 € | 100 € |
| CO₂-/Luftqualitätssensoren | 3 | 30–60 € | 150 € |
| Heizkreis-Aktoren (Thermostatventile/Ventilatoren) | 8 | 20–40 € | 240 € |
| Smart-Relais (Shelly-Klasse, lokal, kein Cloud-Zwang) | 10 | 10–18 € | 140 € |
| Licht (Zigbee/Matter-Lampen + Dimmer) | 15 | 8–20 € | 200 € |
| Smarte Steckdosen (verlagerbare Lasten) | 6 | 8–15 € | 70 € |
| **Summe Sensoren/Aktoren** | | | **~1.400 €** |

(Dazu Netzfrei-Software: 0 € – Home Assistant, Zigbee2MQTT, Mosquitto,
InfluxDB/Grafana, LLM-Laufzeit – alles Open Source.)

## 5. Schichtenmodell von Netzfrei

```
┌──────────────────────────────────────────────┐
│  Ebene 4: KI/Optimierung (MPC, LLM-Assistent)│  ← entscheidet
├──────────────────────────────────────────────┤
│  Ebene 3: Automatisierung (Home Assistant)   │  ← setzt um
├──────────────────────────────────────────────┤
│  Ebene 2: Bus/Gateway (Modbus, Zigbee2MQTT,  │  ← übersetzt
│            Thread-Border-Router, MQTT)       │
├──────────────────────────────────────────────┤
│  Ebene 1: Feldgeräte (Sensoren, Aktoren,     │  ← misst/schaltet
│            Zähler, WP, Batterie)             │
└──────────────────────────────────────────────┘
```

- **Ebene 1–3 sind heute kaufbare Standardware** (Tabelle oben).
- **Ebene 4 ist die eigentliche Netzfrei-Entwicklung**: MPC-Optimierer
  (24-h-Horizont), Prognosemodelle (PV, Bedarf, Preis), LLM-Assistent lokal
  auf dem Homelab, Fallback-Logik bei Ausfall.
- Alles läuft auf **einem Gerät** (Homelab-Server, der ohnehin als
  Abwärmequelle im System steht) – keine zweite Hardware nötig.

## 6. Warum Home Assistant und kein Eigenbau

- 2.500+ fertige Geräteintegrationen sparen Jahre Entwicklungsarbeit.
- Die Optimierung (Ebene 4) wird als **Add-on/Python-App** angedockt und
  liest/schreibt über die HA-API – saubere Trennung, HA bleibt austauschbar.
- Größte Community = dokumentierte Lösungen für jedes Randproblem.
- Lizenz (Apache-2.0) erlaubt kommerzielle Netzfrei-Verbreitung.
