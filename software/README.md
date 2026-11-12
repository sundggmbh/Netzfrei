# Netzfrei-Software

Lokale EMS-Regelung (Energy Management System) für das AUTARQ-System –
ohne Cloud, ohne Abo. **Motto: Einfach, kostengünstig, unabhängig –
für jeden bezahlbar.**

## Architektur (3 Ebenen, siehe docs/03-smart-home-ki.md)

```
┌───────────────────────────────────────────────┐
│ Ebene 3: Netzfrei-KI (später: MPC + lokales   │
│          LLM, Prognosen)                      │
├───────────────────────────────────────────────┤
│ Ebene 2: EMS-Regellogik  ← DIESER CODE (v1)   │
│          netzfrei/ems.py, regelbasiert        │
├───────────────────────────────────────────────┤
│ Ebene 1: Home Assistant (Sensoren/Aktoren,    │
│          Zigbee/Thread/Modbus)                │
└───────────────────────────────────────────────┘
```

## Inhalt

| Pfad | Zweck |
|---|---|
| `netzfrei/ems.py` | EMS-Kern: `Zustand` → `Entscheidung`, Priorisierung Eigenverbrauch → Kosten → Autarkie → Komfort |
| `simulation.py` | Wintertag-Simulation (24 h) zum Testen der Logik ohne Hardware |
| `tests/test_ems.py` | Unit-Tests der Regellogik (stdlib `unittest`) |
| `homeassistant/` | HA-Grundgerüst: `configuration.yaml` + Package `netzfrei.yaml` |

## EMS-Regeln (v1, regelbasiert)

Priorität absteigend – die erste passende Regel gewinnt:

1. **Abtauung** (Verdampfer frostig) → WP aus, Induktion an (docs/15)
2. **Komfort-Notfall** (< 19 °C) → sofort Wärme, egal was der Preis sagt
3. **Kollektor-Lüfter** (Kollektor > Puffer + 8 K) → gratis Wärme ernten
4. **Überschuss** (PV + Server > Verbrauch) → erst Batterie (bis 90 %),
   dann Puffer/WP, dann Folie, dann Einspeisung
5. **Günstiges Preisfenster** (≤ 15 ct) → Puffer laden
6. **Teures Fenster** (≥ 35 ct) → WP aus, aus Puffer/Batterie bedienen
7. **Normalbetrieb** → WP moduliert auf halber Leistung

Jede Entscheidung trägt ihre **Begründung** mit (`Entscheidung.gruende`) –
Vertrauen durch Nachvollziehbarkeit, Grundlage fürs spätere Lernen.

## Ausführen

```bash
python3 -m unittest discover -s software/tests -v
python3 software/simulation.py
```

## Home-Assistant-Anbindung

`homeassistant/` enthält ein minimales Setup mit Package `netzfrei.yaml`
(Sensoren, Helfer für Schwellen, erste Automatik fürs Preisfenster).
Die Schwellen in `ems.py` und die Helfer in HA verwenden dieselben Werte.

## Roadmap (Phase 3 aus docs/04)

- [x] Regelbasierte Optimierung (PV-Überschuss, Preisfenster) ← v1
- [ ] Anbindung an echte Sensoren (Modbus/Zigbee) statt `Zustand`-Mock
- [ ] MPC-Optimierer + lokale Prognosemodelle (PV, Temperatur, Preise)
- [ ] Lokaler LLM-Assistent für Bedienung/Erklärung
- [ ] Netzfrei-System-Image (flashbar für Mini-PC)
