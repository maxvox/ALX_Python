###positional arguments
# def sum(a, b, c):
#     pass


######     keyword arguments
# def increment(value, step):
#     def increment(value: int, step: int = 1) -> int:  # kolejność 1# keyword 2# pozycyjne
#         """
#         Przykład użycia, w parach
#         >>> test
#         wynik testu
#
#         :param value:
#         :param step:
#         :return:
#         """
#         return value + step
#
#
# print(increment(5, 2))  # Outcome: 7    # posługiwanie się pozycją argumentu
# print(increment(5))  # Outcome: 6
# print(increment(value=5, step=2))  # Outcome: 7
# print(increment(step=5, value=1))  # Outcome: 6

#############################################################################
#############################################################################

#### -Napisz testy  -> doctest-

#  postać:   """Docstring"""
# ## Notatka
# utwórz nazwę funkcji 'sygnatura funkcji' > enter > zacznij pisać docstring """ (pierwsze trzy cudzysłowy),
# samo się uzupełni do sześciu, stojąc pomiędzy 3 a 3 naciśnij enter -> samo się wszystko uzupełni na postać:
# """
#
# :param value:
# :param step:
# :return:
# """


#############################################################################
#############################################################################

"""
Bez posługiwania się wbudowanymi funkcjami takimi jak max czy min
napisz funkcję (a może funkcje) która zwróci max z trzech liczb
"""


##>>>>>>>>>>>>>>>>>>>>>   TBD

# from typing import Tuple
#
#
# def wprow_danych(a: int, b: int, c: int) -> Tuple[str, str, str]:
#     liczba_1 = int(input('Wartość pierwsza:  '))
#     liczba_2 = int(input('Wartość druga:  '))
#     liczba_3 = int(input('Wartość trzecia:  '))
#     return liczba_1, liczba_2, liczba_3
#
#
# wprow_danych(1, 1, 1)
#
#
# def dzialania():
#     if wprow_danych(liczba1) > liczba2:


#############################################################################
#############################################################################

def max_of_three2(a: float, b: float, c: float) -> float:
    if (a > b) and (a > c):
        wynik = a
    elif (b > a) and (b > c):
        wynik = b
    else:
        wynik = c
    return wynik

#############################################################################
#############################################################################
#############################################################################


def max_of_two(a, b):
    if a >b:
        return a
    return b

def max_of_three(a, b, c):
    return max_of_two(a,max_of_two(b, c))

if __name__ == "__main__":
    assert max_of_three(1, 3, 2) == 3
    assert max_of_three(2, 6, -5) == 6

#############################################################################
#############################################################################
#############################################################################
















