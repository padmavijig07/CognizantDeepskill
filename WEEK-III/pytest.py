import pytest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

calc = Calculator()

@pytest.fixture
def numbers():
    return (20, 10)

def test_add(numbers):
    a, b = numbers
    assert calc.add(a, b) == 30

def test_subtract(numbers):
    a, b = numbers
    assert calc.subtract(a, b) == 10

def test_multiply(numbers):
    a, b = numbers
    assert calc.multiply(a, b) == 200

def test_divide(numbers):
    a, b = numbers
    assert calc.divide(a, b) == 2

def test_add_negative():
    assert calc.add(-5, 5) == 0

def test_subtract_negative():
    assert calc.subtract(-10, -5) == -5

def test_multiply_zero():
    assert calc.multiply(10, 0) == 0

def test_divide_float():
    assert calc.divide(5, 2) == 2.5

def test_large_numbers():
    assert calc.add(1000, 2000) == 3000

def test_negative_multiply():
    assert calc.multiply(-5, 2) == -10

def test_divide_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)


#pip install pytest pytest-cov
#pytest PyTest.py
#pytest --cov=PyTest PyTest.py