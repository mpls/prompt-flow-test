import pytest
from src.utils import subtract

def test_subtract_integers():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5

def test_subtract_floats():
    assert subtract(10.5, 5.5) == 5.0
    assert subtract(5.5, 2.5) == 3.0
    assert subtract(1.0, 0.1) == pytest.approx(0.9)

def test_subtract_negatives():
    assert subtract(-5, -5) == 0
    assert subtract(-5, 5) == -10
    assert subtract(5, -5) == 10

def test_subtract_zero():
    assert subtract(10, 0) == 10
    assert subtract(0, 10) == -10
    assert subtract(0, 0) == 0
