import unittest
from datetime import date

from engine.willoughbyEngine import WilloughbyEngine

class TestWilloughbyEngine(unittest):
    def test_need_service_true(self):
        current_mileage = 25000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_need_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())    