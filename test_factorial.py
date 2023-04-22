"""Test factorial function"""

import pytest
from factorial import factorial

def test_factorial():
    """Test factorial function with positive integers"""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(10) == 3628800

def test_factorial_negative():
    """Test factorial function with negative integers"""
    with pytest.raises(ValueError):
        factorial(-1)
        factorial(-100)

def test_factorial_non_integer():
    """Test factorial function with non-integer values"""
    with pytest.raises(TypeError):
        factorial(1.5)
        factorial("1")
        factorial([1])
