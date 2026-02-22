import pytest
from src.math import multiply

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6
    assert multiply(10, 5) == 50

def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6
    assert multiply(-2, -3) == 6

def test_multiply_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(0, 0) == 0

def test_multiply_floats():
    assert multiply(2.5, 2) == 5.0
    assert multiply(1.5, 3.0) == 4.5
    assert abs(multiply(0.1, 0.2) - 0.02) < 1e-9  # Floating point comparison
