"""

Napisz program, który będzie realizował proste działania matematyczne.

$ python kalkulator.py

> Jaką operację chcesz wykonać? [1-dodaj, 2-odejmowanie, 3-mnożenie, 4-dzielenie]: 1
> Podaj liczbę 1: 2
> Podaj liczbę 2: 3
Wynik to: 5

"""


# def get_data() -> tuple[str, int, int]:  # 3.10
#     operacja = input("Jaką operację chcesz wykona? [1-dodaj, 2-odejmowanie, 3-mnożenie, 4-dzielenie]:")
#     a = int(input(f"Podaj liczbę 1"))
#     b = int(input("Podaj liczbę 2"))
#     return operacja, a, b


def add(a: int, b: int) -> int:
    """ `add` takes two integers, `a` and `b`, and returns their sum

    Parameters
    ----------
    a : int
        int - This is the first parameter, named a, and it's type is int.
    b : int
        int

    Returns
    -------
        The sum of a and b

    """
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float or str:
    if b == 0:
        return "Nie dziel przez zero"
    return a / b


# It's a dictionary, where the keys are strings, and the values are functions.
operations = {
    "1": add,
    "2": sub,
    "3": mul,
    "4": div
}
# It's printing the type of the variable `operations` and the string `operacja type`.
print(type(operations), 'operacja type')


def kalkulator(operacja: str, a: int, b: int) -> int or str or float:  # 3.10

    """ "If the operation is not in the dictionary, return a string, otherwise return the result of the operation."

    The function is defined with three parameters: operacja, a, and b. The first parameter is a string, the other two are
    integers. The function returns an integer, a string, or a float

    Parameters
    ----------
    operacja : str
    	str - the operation to be performed
    a : int
    	int, b: int - these are the parameters that the function takes.
    b : int
    	int - the second parameter is an integer

    Returns
    -------
    	The result of the operation or a string if the operation is not defined.

    """

    try:
        wynik = operations[operacja](a, b)
    except KeyError:
        wynik = "Nieokreślona operacja"
    return wynik

# if __name__ == "__main__":
#     op, a, b = get_data()
#     assert kalkulator("1", 3, 4) == "Nieokreślona operacja"
