"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_is_instance():
    """Testing Calculator Instance"""
    calculator = Calculator()
    assert isinstance(calculator, Calculator)


def test_calculator_get_result_method():
    """Testing Calculator Get Result"""
    calculator = Calculator()
    assert calculator.get_result() == 0


def test_calculator_result_property():
    """Testing the Calculator's Result Property"""
    calc1 = Calculator()
    calc2 = Calculator()
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6


def test_calculator_add_method():
    """Testing the Calculator's Add Method (0 + 1)"""
    calculator = Calculator()
    assert calculator.add(1) == 1

def test_calculator_subtract_method():
    """Testing the Calculator's Subtract Method (0 - 1)"""
    calculator = Calculator()
    assert calculator.subtract(1) == -1
