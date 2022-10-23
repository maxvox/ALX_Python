from kalkulator2 import add, sub, mul, div, operations, kalkulator

def test_add():
    assert add(1, 2) == 3
    assert add(1, -2) == -1
    assert add(1, 2) == 3
    assert add(1, 2) == 3

def test_sub():
    assert sub(6, 2) == 4

def test_mul():
    assert mul(8, 2) == 16

def test_div():
    assert div(56, 2) == 28


def test_kalkulator():
    assert kalkulator('1', 5, 3) == 8


# assert operations == True

