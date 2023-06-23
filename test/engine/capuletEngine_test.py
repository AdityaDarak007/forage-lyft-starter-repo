import unittest
from datetime import date

from engine.capuletEngine import CapuletEngine

class TestCapuletEngine(unittest):
    def test_need_service_true(self):
        current_mileage = 150000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_need_service_false(self):
        current_mileage = 200000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())    