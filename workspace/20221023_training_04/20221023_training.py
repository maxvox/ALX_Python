###positional arguments
def sum(a, b, c):
    pass


######     keyword arguments
def increment(value, step):
    def increment(value: int, step: int = 1) -> int:  # kolejność 1# keyword 2# pozycyjne
        """
        Przykład użycia, w parach
        >>> test
        wynik testu

        :param value:
        :param step:
        :return:
        """
        return value + step


print(increment(5, 2))  # Outcome: 7    # posługiwanie się pozycją argumentu
print(increment(5))  # Outcome: 6
print(increment(value=5, step=2))  # Outcome: 7
print(increment(step=5, value=1))  # Outcome: 6

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
