"""
Napisz program, który będzie realizował proste działania matematyczne.
$ python kalkulator.py
> Jaką operację chcesz wykonac? [1-dodawanie, 2-odejmowanie, 3-mnożenie, 4-dzielenie]: 1
> Podaj liczbę 1: 2
> Podaj liczbę 2: 3
Wynik to: 5
"""


def get_data() -> tuple[str, int, int]:
    operacja = input('Jaką operację chcesz wykonac? [1-dodawanie, 2-odejmowanie, 3-mnożenie, 4-dzielenie]: ')
    a = int(input('Podaj 1# liczbę: '))
    b = int(input('Podaj 2# liczbę: '))
    return operacja, a, b


def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float:
    return a / b


def kalkulator(operacja, a: int, b: int) -> tuple:
    if operacja == '1':
        wynik = add(a, b)
    elif operacja == '2':
        wynik = sub(a, b)
    elif operacja == '3':
        wynik = mul(a, b)
    elif operacja == '4':
        wynik = div(a, b)
    else:
        print('Nieokreślona operacja.')
        exit()

    return wynik, a, b


# kalkulator('2', 3, 6)
kalkulator()
