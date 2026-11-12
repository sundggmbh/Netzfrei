"""Unit-Tests fuer die Netzfrei-EMS-Regellogik.

Aufruf: python3 -m unittest discover -s software/tests -v
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from netzfrei.ems import (
    BATTERIE_ZIEL_SOC,
    PUFFER_MIN_C,
    PUFFER_SOLL_C,
    Zustand,
    entscheide,
)


def basis(
    stunde=12,
    pv_w=0.0,
    verbrauch_w=500.0,
    batterie_soc=0.5,
    preis_ct=20.0,
    raum=20.5,
    puffer=33.0,
    kollektor=25.0,
    frost=False,
):
    return Zustand(
        stunde=stunde,
        pv_w=pv_w,
        verbrauch_w=verbrauch_w,
        server_w=400.0,
        batterie_soc=batterie_soc,
        preis_ct=preis_ct,
        raum_temp_c=raum,
        puffer_temp_c=puffer,
        kollektor_temp_c=kollektor,
        verdampfer_frost=frost,
    )


class TestEms(unittest.TestCase):
    def test_komfort_notfall_ueberschreibt_alles(self):
        e = entscheide(basis(preis_ct=45, raum=18.5, puffer=40.0))
        self.assertEqual(e.aktion, "komfort_notfall")
        self.assertGreater(e.wp_kw, 0.0)

    def test_komfort_notfall_folie_wenn_puffer_leer(self):
        e = entscheide(basis(preis_ct=45, raum=18.5, puffer=25.0))
        self.assertEqual(e.aktion, "komfort_notfall")
        self.assertEqual(e.wp_kw, 0.0)
        self.assertGreater(e.folie_kw, 0.0)

    def test_abtauung_hat_vorrang_und_stellt_wp_ab(self):
        e = entscheide(basis(frost=True, raum=18.0))
        self.assertEqual(e.aktion, "abtauung")
        self.assertEqual(e.wp_kw, 0.0)
        self.assertGreater(e.induktion_kw, 0.0)

    def test_pv_ueberschuss_laedt_batterie_zuerst(self):
        e = entscheide(basis(pv_w=2500, verbrauch_w=500, batterie_soc=0.5, puffer=40.0))
        self.assertEqual(e.batterie, "laden")
        self.assertEqual(e.aktion, "ueberschuss_batterie")

    def test_pv_ueberschuss_geht_in_waerme_wenn_batterie_voll(self):
        e = entscheide(basis(pv_w=2500, verbrauch_w=500, batterie_soc=BATTERIE_ZIEL_SOC, puffer=30.0))
        self.assertEqual(e.aktion, "ueberschuss_waerme")
        self.assertGreater(e.wp_kw, 0.0)

    def test_ueberschuss_teilt_sich_batterie_und_puffer(self):
        e = entscheide(basis(pv_w=2500, verbrauch_w=500, batterie_soc=0.5, puffer=30.0))
        self.assertEqual(e.aktion, "ueberschuss_batterie_puffer")
        self.assertEqual(e.batterie, "laden")
        self.assertGreater(e.wp_kw, 0.0)

    def test_pv_rest_geht_in_folie(self):
        e = entscheide(basis(pv_w=2500, verbrauch_w=500, batterie_soc=0.95, puffer=40.0, raum=21.0))
        self.assertEqual(e.aktion, "ueberschuss_folie")
        self.assertGreater(e.folie_kw, 0.0)
        self.assertEqual(e.wp_kw, 0.0)

    def test_guenstiges_fenster_laedt_puffer(self):
        e = entscheide(basis(preis_ct=10, puffer=30.0))
        self.assertEqual(e.aktion, "preisfenster_puffer")
        self.assertGreater(e.wp_kw, 0.0)

    def test_teures_fenster_stellt_wp_ab(self):
        e = entscheide(basis(preis_ct=45, puffer=PUFFER_MIN_C + 2))
        self.assertEqual(e.aktion, "teuer_puffer")
        self.assertEqual(e.wp_kw, 0.0)
        self.assertEqual(e.batterie, "entladen")

    def test_komfort_hat_vorrang_vor_teurem_preis(self):
        e = entscheide(basis(preis_ct=45, puffer=25.0, raum=18.5))
        self.assertEqual(e.aktion, "komfort_notfall")

    def test_kollektor_luefter_bei_delta(self):
        e = entscheide(basis(kollektor=45.0, puffer=30.0))
        self.assertTrue(e.kollektor_luefter)
        e2 = entscheide(basis(kollektor=35.0, puffer=30.0))
        self.assertFalse(e2.kollektor_luefter)

    def test_normalbetrieb_moduliert(self):
        e = entscheide(basis(preis_ct=20, puffer=33.0, raum=20.5))
        self.assertEqual(e.aktion, "normal")
        self.assertGreater(e.wp_kw, 0.0)
        self.assertLess(e.wp_kw, 5.0)


if __name__ == "__main__":
    unittest.main()
