# 15 – Induktionswärme: Wärme durch Wirbelströme (Realitätscheck + Nischen)

Idee aus der Diskussion: Wärme „nur durch das Hin-und-Her-Wechseln des Stroms"
(~10.000 Hz) erzeugen wie beim Induktionskochfeld – als eigenes Heizelement im
Haus-System und langfristig als eigenes Produkt für Heizen des Objekts.

## 1. Physik-Realitätscheck (ehrlich zuerst)

**Es ist keine Gratis-Wärme.** Das Induktionsprinzip:

1. Eine Spule führt einen hochfrequenten Wechselstrom (Haushalts-Kochfelder:
   typ. **20–100 kHz**, meist 25–60 kHz; Industrieanlagen 50 Hz–100 kHz).
2. Das magnetische Wechselfeld induziert in einem **ferromagnetischen,
   leitfähigen Bauteil** (Eisen/Stahl – nicht Alu/Kupfer) **Wirbelströme**.
3. Diese fließen wegen des **Skin-Effekts** nur in einer dünnen Randschicht
   (Millimeterbereich) und verheizen sich dort als **Widerstandswärme**;
   zusätzlich entstehen **Ummagnetisierungsverluste** (Hysterese).

Energiebilanz: Der Strom wird **verbraucht** – 1 kWh Strom wird zu
~0,8–0,9 kWh Wärme im Bauteil (Kochfeld-Gesamtwirkungsgrad ~84–90 %, Rest
Verluste in Leistungselektronik und Spule). Das ist **COP ≈ 0,85**:

| Verfahren | COP | Anmerkung |
|---|---|---|
| Wärmepumpe (Low-Lift, `09`) | **8–15** | 1 kWh Strom → 8–15 kWh Wärme |
| Wärmepumpe (Luft/Wasser, Winter) | 3–4 | Standardbetrieb |
| Carbon-Folie/-Farbe (`05`, `07`) | **1,0** | 1 kWh Strom → ~1 kWh Wärme direkt in der Fläche |
| **Induktion** | **~0,85** | 1 kWh Strom → ~0,85 kWh Wärme im ferromagnetischen Bauteil |

**Schlussfolgerung:** Induktion ersetzt weder WP noch Folie als Grundheizung –
als flächige Grundheizung wäre sie sogar etwas schlechter als die Folie
(mehr Elektronik, gleiche Physik). **Aber:** sie hat Eigenschaften, die keine
andere Hebeebene hat. Die sind der Grund, sie als **Hebebene 3b für Nischen**
ins System zu nehmen.

## 2. Was Induktion wirklich gut kann

| Eigenschaft | Bedeutung fürs Haus-System |
|---|---|
| **Kalte Emitterfläche** | Die Spule selbst bleibt kühl; die Wärme entsteht im Bauteil dahinter – keine heißen Drähte, kein Brandrisiko an der Oberfläche |
| **Kontaktlos durch Trennschichten** | Heizen durch nichtleitende/islolierende Barrieren (Keramik, Glas, Dämmung, Tankwand von außen) |
| **Hohe Leistungsdichte, schnelle Regelung** | kW pro kleiner Fläche, millisekundenschnell modulierbar – ideal für Boost- und Schub-Betrieb |
| **Kein Medienkontakt** | Kein Heizstab im Wasser → keine Verkalkung, keine Legionellen-Nische am Heizstab, Tank bleibt dicht |
| **Gezielt ortsfest** | Feld konzentrierbar (Polschuhe/Ferrite) → einzelne Zone/Punkt gezielt beheizen |
| **Kühlung?** | **Nein.** Induktion erzeugt nur Wärme; Kühlen bleibt Aufgabe von WP/KWL (`06`, `11`) |

## 3. Nischen im AUTARQ-System (bewertet)

| Nr. | Anwendung | Nutzen | Bewertung |
|---|---|---|---|
| **N1** | **Induktive Abtauung des WP-Verdampfers** | Statt Umkehrbetrieb oder Heizstab: Verdampferlamellen (Stahl) gezielt in Minuten abtauen, kein Kältemittel-Umschalten, kein Effizienzverlust durch Tauperiode in der Bilanz | ★★★ echte Systemverbesserung, klein (1–2 kW), gut machbar |
| **N2** | **Kontaktlose Erwärmung von Puffer-/Brauchwassertank** (Spule außen am Stahltank, Ferrit-Rückschluss, Dämmung darüber) | Kein Heizstab im Wasser, keine Verkalkung, hygienisch, Tank bleibt geschlossen; PV-Überschuss-Boost in den Puffer | ★★★ einzigartige Eigenschaftskombination |
| **N3** | **Leitungs-Frostschutz** (induktive Beheizung von Stahl-/Verbundrohren in kalten Zonen) | Kontaktlos, nur aktiv wenn nötig, kein Dauer-Heizband | ★★ nützlich, kleiner Aufwand |
| **N4** | **Boost-Heizpanel mit Stahlkern** (Wand/Decke: Spulen hinter nichtmetallischer Abdeckung erwärmen Stahlblech → Strahlung) | Kalte Oberfläche, schnelle Wärme aus PV-Überschuss; aber teurer als Folie bei COP 0,85 vs. 1,0 | ★★ möglich, nur wo Folie nicht geht (Feuchtraum, mechanische Belastung) |
| **N5** | **Warmwasser-Schnellladung** (Power-Boost in den Tank) | Dusche nach Sonnenuntergang ohne WP-Laufzeit | ★★ Komfort-Feature, N2 vorausgesetzt |
| – | **Flächige Grundheizung** | Folie/Farbe machen das gleiche billiger und mit COP 1,0 | ✗ nicht empfohlen |

## 4. Architektur-Integration

```
                    ┌──────────────────────────────┐
  PV-Überschuss ───▶│ Netzfrei-EMS (Priorisierung) │
                    └──┬───────────┬───────────┬───┘
                       │           │           │
             ┌─────────▼──┐  ┌─────▼─────┐  ┌──▼─────────────┐
             │ Hebebene 3a│  │ Hebebene 3b│  │ Hebebene 3b    │
             │ Folie/Farbe│  │ Induktion  │  │ Induktion      │
             │ (COP 1,0)  │  │ Abtauung N1│  │ Tank-Boost N2/N5│
             └────────────┘  └────────────┘  └────────────────┘
                       │           │           │
             Grundwärme/      WP-Verdampfer   Puffer/Brauchwasser
             Zonenheizen      frostfrei       nachladen
```

**Einsatzregeln für Netzfrei (EMS):**

- Grundwärme → Folie/Farbe (billiger, COP 1,0); Induktion nur für N1–N5.
- **N1-Abtauung:** auslösen bei Verdampfer-Frostsensor + sinkender WP-Leistung;
  1–2 kW für 1–3 Minuten statt 10–20 Minuten Umkehrbetrieb.
- **N2/N5-Boost:** nur bei PV-Überschuss oder günstigem Stromfenster
  (gleiche Logik wie Folie, `03-smart-home-ki.md` Priorisierung).
- Induktionsmodule melden Leistung/Frequenz/Temperatur über ESPHome/Modbus
  an Netzfrei (gleiche Schnittstelle wie Kollektor, `12` Kap. 6).

## 5. Technische Skizze (BOM pro Modul, grob)

| Bauteil | Spezifikation | Kosten (DIY, Stück) |
|---|---|---|
| Resonanz-Halbbrücken-Wandler | 1–2 kW, 25–60 kHz, IGBT/SiC-Modul oder fertiges Kochfeld-Powerboard | 40–120 € |
| Arbeitsspule | Litzendraht, 10–30 Windungen, formangepasst (Tank zylindrisch / Lamellen flach) | 15–40 € |
| Ferrit-Rückschluss | konzentriert das Feld, schützt Umgebung | 10–30 € |
| Resonanzkondensatoren | MKP-Filmkondensatoren, spannungsfest | 10–25 € |
| Temperatur-/Stromsensing | NTC + Shunt/Hall, ESP32 | 10–20 € |
| Gehäuse/Isolation | Keramik-/Glasabdeckung, Kriechstrecken | 20–50 € |
| **Summe je 1–2-kW-Modul** | | **~105–285 €** |

Referenz: fertige Induktionskochfeld-Zonen (1,8–3,5 kW) kosten 30–60 €/Zone –
die Leistungselektronik ist damit **Serienware**; unsere Modifikation ist
Spulenform + Anbindung + Regelung, kein Neuerfinden.

## 6. Produktidee „InductCore“ (Arbeitstitel, später)

- **Produkt 1 – Abtau-Kit:** induktives Abtaumodul für Luft/Wasser-WP
  (retrofit an Standard-Verdampfern) – verkauft sich an jeden WP-Betreiber
  mit Tauproblemen; kleines, klar messbares Ziel.
- **Produkt 2 – Tank-Boost-Kit:** Spulenring + Wandler zum Nachrüsten an
  Stahl-Puffer/Boilern (PV-Überschuss-Boost ohne Heizstab).
- **Positionierung:** Nischenprodukte **neben** SunWall; erst nach P4
  (SunWall etabliert) angehen. Beide nutzen die gleiche Leistungselektronik.
- **Ehrlich:** Kein Massenmarkt wie SunWall; der Wert liegt in der
  Netzfrei-Integration (Abtau- und Boost-Logik), nicht im Bauteil.

## 7. Risiken und Grenzen

- **COP 0,85 < 1,0:** niemals als Grundheizung einsetzen – nur Nischen.
- **EMV/Störabstrahlung:** Hochfrequenz-Felder stören Elektronik in der
  Nähe (inkl. unsere eigene Netzfrei-Hardware!) → Abstände, Abschirmung,
  Zulassung (EN 55014, EN 62233) einplanen; Frequenzwahl mit Rücksicht auf
  Funkdienste.
- **Magnetfelder + Personen:** ICNIRP-Grenzwerte beachten; Spulen hinter
  Abdeckung mit Ferritführung, keine Kopf-/Körpernähe bei Dauerbetrieb.
- **Nur ferromagnetische Bauteile:** Alu-Tanks, Kupferleitungen und
  nichtmetallische Oberflächen sind nicht induzierbar (oder nur über
  aufgeklebte Stahlfolien).
- **Skin-Effekt:** Wärme entsteht nur in der Randschicht – für gleichmäßige
  Flächenheizung ist Folie physikalisch überlegen.
- **Regulatorik:** induktive Abtauung am Kältekreis berührt Druckgeräte-
  richtlinie/Kälteanlagen-Verordnung → nur als Zusatzheizung außen am
  Lamellenpaket, nicht in den Kältemittelkreis eingreifen.

## 8. Nächste Schritte

- [ ] N1-Abtauung als erster Prototyp: Kochfeld-Powerboard + flache Spule an
      einen Alt-Verdampfer, Abtauzeit vs. Umkehrbetrieb messen
- [ ] N2-Tanktest: Spulenring an Stahl-Puffer, Wirkungsgrad (Strom → Wärme im
      Wasser) messen; Ziel ≥ 80 %
- [ ] EMV-Vorprüfung (Abstände zu ESP32/Netzfrei-Hardware dokumentieren)
- [ ] Rechner: `--induktion-w` setzt N1–N5 als Nischen-Boost (kein
      Grundheizungs-Anteil) – Auswirkung auf WP-Laufzeit sichtbar machen
