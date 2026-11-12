# 04 – Kosten & Roadmap

## 1. Investitionskosten (Richtwerte, Stand 2025)

Beispiel: Neubau, 120 m², 4 Personen, gemäßigtes Klima, Homelab 400 W.
Werte sind Grobschätzungen inkl. Material, ohne staatliche Förderung;
Selbstbau/DIY senkt die unteren Grenzen weiter.

| Posten | Serien-/Standardpreis | DIY-/Second-Life-Preis |
|---|---|---|
| PV 6 kWp (Dach, inkl. WR) | 5.000–7.000 € | 2.500–4.000 € |
| Batterie 10 kWh | 2.500–4.000 € | 1.500–2.500 € (Second-Life-Zellen) |
| Kompakte Wärmepumpe 1–10 kW | 3.000–6.000 € | 5.000–7.000 € (Einzel-Prototyp) |
| Pufferspeicher 500 l | 400–800 € | 400–800 € |
| Homelab-Server + Netzfrei-Hardware (KI-Heimnetzwerk) | 1.000–2.000 € | 700–1.500 € |
| Smart-Home-Sensoren/Aktoren | 800–2.000 € | 500–1.200 € |
| Hydraulik/Installation | 2.000–4.000 € | 800–2.000 € (Eigenleistung) |
| Carbon-Heizfolie/IR 80 m² (Hybrid, siehe `05-…`) | 1.700–2.500 € | 1.700–2.500 € |
| Lüftung mit WRG + F9-Filter (siehe `06-…`) | 2.600–4.500 € | 1.000–2.100 € (DIY) |
| **Summe** | **~17.000–33.000 €** | **~12.000–21.000 €** |

**Vergleich:** Eine konventionelle Öl-/Gas-Heizung plus Netzanschluss und
Netzstromkosten über 20 Jahre liegen bei vergleichbaren Gebäuden oft bei
30.000–50.000 € laufenden Kosten. Die Autarkie-Investition amortisiert sich
je nach Region in 8–15 Jahren – in sonnenreichen Regionen schneller.

**Betriebskosten nach Umstellung:** ~0 € Netzstrom; Wartung WP ~100–200 €/Jahr.

## 2. Warum das für jeden leistbar ist

- **Neubau-Integration:** Fußbodenheizung, Dämmung und Leitungen sind im Neubau
  ohnehin eingeplant – das System kostet dann nur die *Differenz* (WP + PV +
  Batterie + EMS), nicht den vollen Betrag.
- **Modularer Ausbau:** Stufe 1 (Balkon-PV + Smart Metering) ab ~1.000 €,
  Stufe 2 (+ Batterie) ab ~3.500 €, Stufe 3 (+ WP + Puffer) ab ~8.000 €,
  Stufe 4 (+ Heizfolie + Lüftung, voll autark) ab ~12.000 € DIY.
- **Server als Erwerbsquelle:** Die Rechenlast kann (optional) verkauft werden
  (verteiltes Rechnen, lokale KI-Dienste) – der Server finanziert sich selbst
  und liefert zugleich die Heizung.

## 3. Roadmap

### Phase 1 – Konzept & Auslegung (aktuell)
- [x] Systemarchitektur, Komponenten, Klimazonen
- [x] Auslegungsrechner (`tools/auslegung.py`)
- [ ] Validierung mit realen Referenzgebäuden in allen drei Klimazonen

### Phase 2 – Prototyp Wärmepumpe
- [ ] Detailkonstruktion (CAD), Stückliste, Kältetechnik-Prüfung
- [ ] Prototypenbau Variante A (Luft/Wasser-Monoblock im Therme-Format)
- [ ] Prüfstand: COP/SEER-Messung, Geräusch, Sicherheitszertifizierung (R290)

### Phase 3 – Netzfrei (Energieleitsystem)
- [ ] Home-Assistant-Basisinstallation + Modbus-Anbindung WP/Batterie
- [ ] Regelbasierte Optimierung (PV-Überschuss, Preisfenster)
- [ ] MPC-Optimierer + lokale Prognosemodelle
- [ ] Lokaler LLM-Assistent für Bedienung
- [ ] Netzfrei-System-Image (flashbar für Mini-PC/Homelab)

### Phase 4 – Pilotinstallationen
- [ ] 1 Neubau gemäßigtes Klima (Referenz: Deutschland/Österreich)
- [ ] 1 Gebäude warmes Klima (Kühlung im Fokus)
- [ ] 1 Gebäude kaltes Klima (Heizen im Fokus)
- [ ] Messdatenerfassung & Veröffentlichung der Ergebnisse

### Phase 5 – Verbreitung
- [ ] **SunWall-Produktlinie** (Sonnen-Luftkollektor als eigene Marke, siehe
      `13-produkt-sunwall.md`): Prototyp → Kleinserie → Onlineshop
- [ ] Open-Hardware-Dokumentation (Bauanleitungen, Stücklisten)
- [ ] Partner für Serienfertigung der kompakten WP
- [ ] Anleitung für Selbstbauer in allen Klimazonen
