# It imports the functions add, sub, mul, div, operations and kalkulator from the file kalkulator2.py.
from kalkulator2 import add, sub, mul, div, operations, kalkulator


def test_add():
    # Testing if the function add(1, 2) returns 3.
    assert add(1, 2) == 3
    # Testing if the function add(1, -2) returns -1.
    assert add(1, -2) == -1
    # Testing if the function add(1, 2) returns 3.
    assert add(1, 2) == 3
    # Testing if the function add(1, 2) returns 3.
    assert add(1, 2) == 3


def test_sub():
    # Testing if the function sub(6, 2) returns 4.
    assert sub(6, 2) == 4


def test_mul():
    # Testing if the function mul(8, 2) returns 16.
    assert mul(8, 2) == 16


def test_div():
    # Testing if the function div(56, 2) returns 28.
    assert div(56, 2) == 28


def test_kalkulator():
    # Testing if the function kalkulator('1', 5, 3) returns 8.
    assert kalkulator('1', 5, 3) == 8


def test_operations():
    # Checking if the dictionary operations is equal to the dictionary {"1": add, "2": sub, "3": mul, "4": div}.
    assert operations == {"1": add, "2": sub, "3": mul, "4": div}
