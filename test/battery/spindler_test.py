import unittest
from datetime import date

from battery.spindlerbattery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_need_service_true(self):
        current_date = date.fromisoformat("2022-06-23")
        last_service_date = date.fromisoformat("2022-01-01")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_need_service_false(self):
        current_date = date.fromisoformat("2022-06-23")
        last_service_date = date.fromisoformat("2020-01-21")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
