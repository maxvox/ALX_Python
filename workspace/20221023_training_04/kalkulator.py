"""
Napisz program, który będzie realizował proste działania matematyczne.
$ python kalkulator.py
> Jaką operację chcesz wykonac? [1-dodawanie, 2-odejmowanie, 3-mnożenie, 4-dzielenie]: 1
> Podaj liczbę 1: 2
> Podaj liczbę 2: 3
Wynik to: 5
"""
if __name__ == '__main__':

    def kalkulator(operacja, liczba1: int, liczba2: int) -> int:
        operacja = input('Jaką operację chcesz wykonac? [1-dodawanie, 2-odejmowanie, 3-mnożenie, 4-dzielenie]: ')
        liczba1 = int(input('Podaj 1# liczbę: '))
        liczba2 = int(input('Podaj 2# liczbę: '))

################# zaprzeczenia nie działają, do poprawy
        if operacja <= '0' or operacja >= '5':
            print('Nieznana operacja.')

        if liczba1 != int:
            print('Nieznana operacja.')

        if liczba2 != int:
            print('Nieznana operacja.')

        if operacja == '1':
            print(liczba1 + liczba2)
        elif operacja == '2':
            print(liczba1 - liczba2)
        elif operacja == '3':
            print(liczba1 * liczba2)
        elif operacja == '4':
            print(liczba1 / liczba2)
        else:
            exit()

        return operacja, liczba1, liczba2


    kalkulator('2', 3, 6)
