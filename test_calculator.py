import calculator
import pytest

def test_add_positive_numbers():
    assert calculator.add(5, 3) == 8
    
def test_subtract_numbers():
    assert calculator.subtract(10, 4) == 6

def test_multiply_numbers():
    assert calculator.multiply(4, 5) == 20

def test_divide_numbers():
    assert calculator.divide(20, 4) == 5

def test_add_negative_numbers():
    assert calculator.add(-5, -3) == -8

def test_add_zero():
    assert calculator.add(7, 0) == 7
    
def test_multiply_by_zero():
    assert calculator.multiply(9, 0) == 0
    
def test_subtract_negative():
    assert calculator.subtract(5, -3) == 8

def test_divide_negative():
    assert calculator.divide(-20, 4) == -5
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)
