import pytest
import calculator
from dotenv import load_dotenv
import os

def test_add():
    print("Adding two numbers. Number 1: 1, Number 2: 2")
    assert calculator.add(1, 2) == 3

def test_subtract():
    assert calculator.subtract(1, 2) == -1

def test_multiply():
    load_dotenv()
    print(os.getenv("TEST_KEY"))
    assert calculator.multiply(1, 2) == 0

def test_divide():
    load_dotenv()
    print(os.getenv("UNIQUE_ID"))
    assert calculator.divide(1, 2) == 0.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
