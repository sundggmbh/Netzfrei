# SunWall-Webseite (statisch)

Verkaufsfertige Vorvermarktungs-Seite: Warteliste + Produkte + Förder-Check + FAQ.
Statisches HTML/CSS mit einer kleinen clientseitigen JS-Auswertung im Förder-Check –
**keine Build-Tools, keine Abhängigkeiten, kein Tracking** (Förder-Check läuft rein im
Browser).

## Lokal ansehen

```bash
cd website
python3 -m http.server 8080
# Browser: http://localhost:8080
```

## Veröffentlichen (GitHub Pages)

1. Repository-Settings → Pages → Source: Branch `vibe/projektgrundlage-d22643`,
   Ordner `/website` (bzw. nach Merge: `main`, Ordner `/website`).
2. Später eigene Domain aufschalten (CNAME-Datei ergänzen).

Alternativ überall dort deploybar, wo statische Dateien laufen (Netlify, Cloudflare
Pages, jeder Webserver).

## Vor dem Launch (Pflicht, siehe `docs/17-go-to-market.md` Kap. 4)

- [ ] `impressum.html`: Firmenangaben eintragen (DDG § 5)
- [ ] `datenschutz.html`: an tatsächliche Verarbeitung anpassen (Hosting, E-Mail)
- [ ] Bestell-E-Mail-Adresse `bestellung@example.org` in `index.html` ersetzen
- [ ] AGB + Widerrufsbelehrung ergänzen (Pflicht beim Verkauf)
- [ ] CE-/RoHS-Nachweise des Ventilator-Lieferanten einsammeln
- [ ] „Zielwerte“-Kennzeichnung durch Messwerte ersetzen, sobald Prüfstand läuft
- [ ] Domain + DPMA-Anmeldung „SunWall“/„Netzfrei“ vor Werbeschaltung

## Struktur

| Datei | Inhalt |
|---|---|
| `index.html` | Landingpage: Motto, Kennzahlen, Warteliste (Charge 1: 50 Module) |
| `produkte.html` | SW-1.0 / SW-2.0 (SW-U/SW-G) / SW-Solar / SW-Wand, Technikdaten |
| `foerdercheck.html` | 5-Fragen-Förder-Check (clientseitig, ohne Gewähr) |
| `faq.html` | Ertrag, Grenzen, Kühlung, Förderung, Montage, Garantie |
| `impressum.html`, `datenschutz.html` | Platzhalter mit TODO-Markern |
| `style.css` | Ein Design-File, mobilfähig, ohne Framework |
