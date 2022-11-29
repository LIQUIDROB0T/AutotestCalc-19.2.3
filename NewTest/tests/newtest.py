import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_subtraction_correct(self):
        assert self.calc.subtraction(self, 2, 2) == 0

    def test_adding_failed(self):
        assert self.calc.adding(self, 2, 2) == 4
