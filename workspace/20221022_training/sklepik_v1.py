
"""
Napisz program wyliczający kwotę należną za zakupiony towar na
podstawie podanej przez użytkownika wagi i nazwy produktu. Do
przechowywania informacji o cenie za kilogram danego produktu
użyj słownika. Wypisz wszystkie dostępne produkty w sklepie


Przykład działania:
ver 1

$ python sklepik.py

Witaj w warzywniaku.
Oferujemy:

- marchew: 3.00 PLN / kg
- ziemniaki: 5 .00 PLN / KG

Co chcesz kupić?   $ marchew
Ile chcesz kupić (kg) - marchew?  -> $ 2.5

Należy się:
7.50 PLN


ver. dalsze.
1. umożliwienie kupienia większej ilości towaru (while True)
2. drugi słownik, stan magazynowy, ile mamy jakiego produktu, żebyu nie kupić więcej niż mamy
    a) powiększanie stanu
    b) dodawanie nowych produktów
"""

###  PODSTAWOWA WERSJA

shop_items = {
    'marchew': 3.00,
    'ziemniaki': 5.00
}

jednostka = 'PLN / kg'

print('Witaj w Warzywniaku! :) ')
print('Oferujemy:')
for product, cena in shop_items.items():
    print(f'{product} {cena} {jednostka}')

pytanie01 = input('\n Co chcesz kupić? ')
pytanie02 = input(f'Ile chcesz kupić (kg)  ({pytanie01}):  ')

if pytanie01 == 'marchew':
    sum_payment = float(pytanie02) * shop_items.get('marchew')
    print(f'Należy się: {sum_payment} PLN')
    if pytanie01 == 'ziemniaki':
        sum_payment = float(pytanie02) * shop_items.get('ziemniaki')
        print(f'Należy się: {sum_payment} PLN')