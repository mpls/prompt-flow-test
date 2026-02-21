import pytest
from src.utils import add

def test_add_integers():
    assert add(1, 2) == 3.0

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_add_negative_numbers():
    assert add(-1, -1) == -2.0
    assert add(-1, 1) == 0.0

def test_add_zero():
    assert add(0, 0) == 0.0
    assert add(5, 0) == 5.0
    assert add(0, 5) == 5.0
