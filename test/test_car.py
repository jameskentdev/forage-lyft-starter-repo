import unittest
from datetime import datetime, timedelta

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestBatteries(unittest.TestCase):
    def test_spindler_true(self):
        battery = SpindlerBattery(
            datetime.now() - timedelta(days=1096), datetime.now())

        self.assertTrue(battery.needs_service())

    def test_spindler_false(self):
        battery = SpindlerBattery(
            datetime.now() - timedelta(days=365), datetime.now())

        self.assertFalse(battery.needs_service())

    def test_nubbin_true(self):
        battery = NubbinBattery(
            datetime.now() - timedelta(days=1460), datetime.now())

        self.assertTrue(battery.needs_service())

    def test_nubbin_false(self):
        battery = NubbinBattery(
            datetime.now() - timedelta(days=365), datetime.now())

        self.assertFalse(battery.needs_service())


class TestEngines(unittest.TestCase):
    def test_capulet_true(self):
        engine = CapuletEngine(20000, 50000)

        self.assertTrue(engine.needs_service())

    def test_capulet_false(self):
        engine = CapuletEngine(20000, 40000)

        self.assertFalse(engine.needs_service())

    def test_willoughby_true(self):
        engine = WilloughbyEngine(20000, 80000)

        self.assertTrue(engine.needs_service())

    def test_willoughby_false(self):
        engine = WilloughbyEngine(20000, 40000)

        self.assertFalse(engine.needs_service())

    def test_sternman_true(self):
        engine = SternmanEngine(True)

        self.assertTrue(engine.needs_service())

    def test_sternman_false(self):
        engine = SternmanEngine(False)

        self.assertFalse(engine.needs_service())


class TestTires(unittest.TestCase):
    def test_carrigan_true(self):
        tire = CarriganTire()

        self.assertTrue(tire.needs_service())

    def test_carrigan_false(self):
        tire = CarriganTire()

        self.assertFalse(tire.needs_service())

    def test_octoprime_true(self):
        tire = OctoprimeTire()

        self.assertTrue(tire.needs_service())

    def test_octoprime_false(self):
        tire = OctoprimeTire()

        self.assertFalse(tire.needs_service())
