"""Netzfrei-Wintertag-Simulation: 24 h regelbasiertes EMS ohne Hardware.

Nur Python-Standardbibliothek. Aufruf:
    python3 software/simulation.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from netzfrei.ems import (
    KOMFORT_MAX_C,
    KOMFORT_MIN_C,
    PUFFER_MIN_C,
    PUFFER_SOLL_C,
    Zustand,
    entscheide,
)

PV_MAX_W = 3000.0
SERVER_W = 400.0
BATTERIE_KWH = 10.0
WP_COP = 4.0

VERBRAUCH_PROFIL_W = [
    250, 230, 220, 220, 240, 350, 600, 800, 700, 500, 450, 480,
    500, 480, 460, 500, 650, 900, 1100, 1000, 800, 600, 400, 300,
]
PREIS_PROFIL_CT = [
    11, 10, 10, 11, 12, 14, 18, 22, 24, 22, 20, 19,
    18, 18, 19, 22, 30, 45, 48, 44, 32, 22, 16, 12,
]


def pv_w(stunde: int) -> float:
    if 7 <= stunde <= 17:
        import math

        return PV_MAX_W * math.sin(math.pi * (stunde - 7) / 10.0)
    return 0.0


def main() -> int:
    raum = 20.5
    puffer = 32.0
    kollektor = 20.0
    soc = 0.5
    strom_kwh = 0.0
    pv_genutzt_kwh = 0.0

    print("=" * 78)
    print("Netzfrei – Wintertag-Simulation (regelbasiertes EMS v1)")
    print(f"Komfort {KOMFORT_MIN_C:.0f}-{KOMFORT_MAX_C:.0f} C | Puffer {PUFFER_MIN_C:.0f}-{PUFFER_SOLL_C:.0f} C | "
          f"Batterie {BATTERIE_KWH:.0f} kWh | Server {SERVER_W:.0f} W")
    print("=" * 78)
    header = f"{'Std':>3} {'PV W':>6} {'Preis':>6} {'Raum':>5} {'Puffer':>6} {'SoC':>5} {'WP kW':>6} {'Folie':>6} {'Battr':>9}  Aktion"
    print(header)
    print("-" * 78)

    for h in range(24):
        z = Zustand(
            stunde=h,
            pv_w=pv_w(h),
            verbrauch_w=VERBRAUCH_PROFIL_W[h],
            server_w=SERVER_W,
            batterie_soc=soc,
            preis_ct=PREIS_PROFIL_CT[h],
            raum_temp_c=raum,
            puffer_temp_c=puffer,
            kollektor_temp_c=kollektor,
        )
        e = entscheide(z)

        waermekw = e.wp_kw + e.folie_kw + e.induktion_kw
        verlust_kw = 0.6 if PREIS_PROFIL_CT[h] < 30 else 0.8
        raum += (waermekw - verlust_kw) * 0.10
        raum = min(max(raum, 17.0), 23.0)

        if e.wp_kw > 0:
            puffer += e.wp_kw * 0.8
        puffer -= 0.5
        if e.kollektor_luefter:
            puffer += 0.4
            kollektor = max(kollektor - 5.0, 15.0)
        else:
            kollektor = max(kollektor - 1.0, 12.0) if h < 8 or h > 17 else kollektor + 2.0
        puffer = min(max(puffer, 20.0), 45.0)

        ueberschuss_kw = (z.pv_w + z.server_w - z.verbrauch_w) / 1000.0
        if e.batterie == "laden":
            soc = min(soc + max(ueberschuss_kw, 0.0) * 0.9 / BATTERIE_KWH, 1.0)
        elif e.batterie == "entladen":
            soc = max(soc - VERBRAUCH_PROFIL_W[h] / 1000.0 / BATTERIE_KWH, 0.0)

        strom_kwh += (
            e.wp_kw / WP_COP + e.folie_kw + e.induktion_kw
            + VERBRAUCH_PROFIL_W[h] / 1000.0
        )
        pv_genutzt_kwh += min(z.pv_w, VERBRAUCH_PROFIL_W[h] + e.wp_kw * 1000.0 / WP_COP) / 1000.0

        print(f"{h:>3} {z.pv_w:>6.0f} {z.preis_ct:>5.0f}c {raum:>5.1f} {puffer:>6.1f} "
              f"{soc:>5.0%} {e.wp_kw:>6.1f} {e.folie_kw:>6.1f} {e.batterie:>9}  {e.aktion}")

    print("-" * 78)
    print(f"Strombedarf gesamt : {strom_kwh:6.1f} kWh (WP inkl. COP {WP_COP})")
    print(f"PV direkt genutzt  : {pv_genutzt_kwh:6.1f} kWh")
    print(f"Raumtemperatur     : {raum:.1f} C (Komfortband {KOMFORT_MIN_C:.0f}-{KOMFORT_MAX_C:.0f} C)")
    print("=" * 78)
    print("Hinweis: stark vereinfachtes thermisches Modell zur Logik-Demonstration.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
