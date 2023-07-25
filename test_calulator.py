import pytest
import calculator
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger('__name__')

def test_add():
    print("Adding two numbers. Number 1: 1, Number 2: 2")
    assert calculator.add(1, 2) == 3

def test_subtract():
    response = {"code":2,"message":"The provided credential information is invalid","payload":None}
    raise Exception(f'Subtract failed: {response}')
    # assert calculator.subtract(1, 2) == -1

def test_multiply():
    load_dotenv()
    print(os.getenv("TEST_KEY"))
    logger.info("This will be displayed")
    assert calculator.multiply(1, 2) == 0

def test_divide():
    logger.info("This will be displayed")
    assert calculator.divide(1, 2) == 0.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
