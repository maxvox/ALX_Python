# lista = [1, 2, 3, 4]
# tupla = ('a', 'b')
# slownik = {
#     1:'a',
#     's':'t',
#     's': ['w', 'r'],
#     set: {4, 5, 6, 7}
#
# }
# set = {2, 3, 4, }
#
#
# print(tupla[1])
# print(type(tupla))
# print(lista, '\n', tupla, '\n', slownik, '\n')


###############################################################################
###############################################################################
# litery_dict = {
#     'a' : '1',
#     'b' : '2',
#     'c' : '3',
#     'd' : '4',
#     'e' : '5'
# }
#
# litery_dict['d'] = 10
#
# try:
#     print(litery_dict['d'])
# except KeyError:
#     print('Nie ma takiego klucza.')
#
# litery_dict['d'] = litery_dict.get('d', 0) + 1
#
# print(litery_dict)


###############################################################################
###############################################################################

###### Zadanie: licznik liter -> słownik z poszczegolnymi literami ze stringu

###### versja -0-

# string_string = 'Ala ma kota'
#
# # string_string2 = ('Ala ma kota',)
#
# dict_dict = {}
# for letter in string_string:
#     dict_dict[letter] = dict_dict.get(letter, 0) +1
# print(dict_dict)


## print(type(string_string))    # string
## print(type(string_string2))   # tuple

# print('keys', dict_dict.keys())
# print('values', dict_dict.values())
# print('items', dict_dict.items())


###### versja -1-
# zliczenia = {}
# for letter in string_string:
#     if letter in zliczenia:
#         zliczenia[letter] += 1
#     else:
#         zliczenia[letter] = 1
#
# print(zliczenia)  ## wrong, to be correct

# # ###### versja -2-
# zliczenia = {}
# for letter in string_string:
#     try:
#         zliczenia[letter] += 1
#     except KeyError:
#         zliczenia[letter] =1
#
# print(zliczenia)

# ###### versja -3-

# TBD


# ###### versja -4-

# from collections import defaultdict
#
# zliczenia = defaultdict(int)
#
# for letter in string_string:
#     zliczenia[letter] += 1
#
# print(zliczenia)
# print(dict(zliczenia))

# ###### versja -5-

# from collections import Counter
#
# zliczenia = Counter(string_string)
# print(zliczenia)
# print(dict(zliczenia))

# ###### versja -6-

# zliczenia = {}
#
# for letter in string_string:
#     zliczenia[letter] = string_string.count(letter)
#
# print(zliczenia)

# ###### versja -7-

# zliczenia = {}
# i = 0
#
# for letter in set(string_string):
#     zliczenia[letter] = string_string.count(letter)
#     i += 1
#
# print(zliczenia)
# print(i)


###############################################################################
###############################################################################
# string_string = 'Ala ma kota'
# string_string2 = ('Ala ma kota',)
# #
# dict_dict = {}
# for letter in string_string:
#     dict_dict[letter] = dict_dict.get(letter, 0) + 1
# print(dict_dict)
#
# print(type(string_string))  # string
# print(type(string_string2))  # tuple
# print('keys', dict_dict.keys())   ### keys dict_keys(['A', 'l', 'a', ' ', 'm', 'k', 'o', 't'])
# print('values', dict_dict.values())   ### values dict_values([1, 1, 3, 2, 1, 1, 1, 1])
# print('items', dict_dict.items())   ### items dict_items([('A', 1), ('l', 1), ('a', 3), (' ', 2), ('m', 1), ('k', 1), ('o', 1), ('t', 1)])
# #
# ### -tworzenie słownika-
# dict_tworzenie = dict([('a', 1), ('c', 3), ('b', 2)])
# print(dict_tworzenie)
# print(type(dict_tworzenie))
#
# klucze = [1, 2, 3, 4]
#
# d = dict.fromkeys(klucze,
#                   30)  ### -> zmienia wartość wszystkich wartości dla wszystkich kluczy na wartość 'value' -> drugi argument -liczbowy
# print('dict.fromkeys(klucze, 1) ', d)
#
# for k, v in dict_tworzenie.items():
#     print(k, v)
#
# print(dict_tworzenie.items())


###############################################################################
###############################################################################



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
#
# shop_items = {
#     'marchew': 3.00,
#     'ziemniaki': 5.00
# }
#
# jednostka = 'PLN / kg'
#
# print('Witaj w Warzywniaku! :) ')
# print('Oferujemy:')
# for product, cena in shop_items.items():
#     print(f'{product} {cena} {jednostka}')
#
# pytanie01 = input('\n Co chcesz kupić? ')
# if pytanie01 != ([shop_items.keys()][0]) or pytanie01 != ([shop_items.keys()][1]):
#     print('Nie mamy takich produktów')
#     exit()
# pytanie02 = input(f'Ile chcesz kupić (kg)  ({pytanie01}):  ')
#
# # def obliczenia():
# if pytanie01 == 'marchew':
#     sum_payment = float(pytanie02) * shop_items.get('marchew')
#     print(f'Należy się: {sum_payment} PLN')
#     if pytanie01 == 'ziemniaki':
#         sum_payment = float(pytanie02) * shop_items.get('ziemniaki')
#         print(f'Należy się: {sum_payment} PLN')
#



###############################################################################
###############################################################################


# A = {1, 2, 3, 4, 5}
# B = {6, 7, 3, 9, 4}
# print(A.symmetric_difference(B))
# print(dir(A))
# print(type(A)) # <class 'set'>
#
# print(A | B)   # {1, 2, 3, 4, 5, 6, 7, 9}
# print(A & B)   # {3, 4}
# print(A - B)   # {1, 2, 5}
# print(A - B)   # {1, 2, 5}
# print(A ^ B)   # {1, 2, 5, 6, 7, 9}



###############################################################################
###############################################################################
"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych
przez użytkownika. Sprawdź jak dużo z tych liczb jest liczbami
parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora
iloczynu.
"""

# liczby_podane = input('Wprowadź liczbę: ')
# if liczby_podane != float:
#     print('Błędna wartość.')
# elif liczby_podane % 2 == 0:
#         print('ok')

# liczby_parz_1do100 = set(range(1,100, 2))
#
# liczby = set()
#
# while True:
#     liczba = input('Wprowadź liczbę lun k, żeby zakończyć: ')
#     if liczba =='k':
#         break
#
#     # liczba = int(liczba)
#     # try:
#     liczby.add(int(liczba))
#     # except
#
# print(f'Ilość unikalnych liczb : {len(liczby)}')
# print(f'Z czegop parzystych od 0 do 100 : {len(liczby & liczby_parz_1do100)}')
#
# x = frozenset([1,2,3,4,5,6,7])
# print(x)

###############################################################################
###############################################################################

# print({x for x in range(100) if x % 3 == 0 },
#       ' \n',
#       {x:x**2 for x in range(100) if x % 3 == 0},
#       )


###############################################################################
###############################################################################

"""
Napisz program, który posortuje liczby w liście
przy wykorzystaniu algorytmu
"Sortowanie przez wybieranie"
"""
# lista = [9, 1, 6, 8, 4, 3, 2, 0]
# # assert lista == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista.sort(reverse=False)
# print(lista)
# lista.sort(reverse=True)
# print(lista)


#  https://pl.wikipedia.org/wiki/Sortowanie_przez_wybieranie

#### -ver 1-

# def wypisz(tab): #tworzymy metode do wypiswania zawartosci naszej tablicy
#     for el in tab:
#         print(el, end=" | ")
# def sortuj_wybor(tab, n):
#     for x in range(n-1): #iterujemy poprzez wszsytkei elementy tablicy, poza ostatnim
#         minimum = x #usatwiamy aktualny element jako ten najmniejszy
#         for j in range(x+1, n):  #a nastepnie szukamy elementow od niego mniejszych
#             if tab[j] < tab[minimum]:
#                 minimum = j
#         if x != minimum: #jezeli znajdziemy element jakkolwiek mniejszy
#             print ("\nKrok ", (x+1), ": wstawianie elementu minimalnego ", tab[minimum], " na pozycje ", x)
#             pom = tab[x] #dokonujemy jego zamiany
#             tab[x] = tab[minimum]
#             tab[minimum] = pom
#
#
# print("Podaj ilosc elementow tablicy:")
# a = int(input())
# tablica = []
# for i in range(a):
#     print("Podaj element nr. ", (i+1))
#     tablica.append(int(input()))
# print("Oto twoja tablica:")
# wypisz(tablica)
# sortuj_wybor(tablica, a)
# print("Oto twoja tablica po sortowaniu:")
# wypisz(tablica)

#### -ver 2-

# lista = [9, 1, 6, 8, 4, 3, 2, 0]
#
# def sortowanie(tab):
#     for z in range(len(tab)):
#         for z in range(len(tab)):
#             najm = z
#             for x in range(z,len(tab)):
#                 if tab[najm]>tab[x]:
#                     najm = x
#
#             tab[z], tab[najm] = tab[najm], tab[z]
#         return tab
# print(sortowanie(lista))


#### -ver 3-

lista = [9, 1, 6, 8, 4, 3, 2, 0]
print(lista)

for i_podstawienia in range(len(lista)):
    i_min_wartosci = i_podstawienia
    for i_ogona in range(i_podstawienia+1, len(lista)):
        if lista[i_ogona] < lista[i_min_wartosci]:
            i_min_wartosci = i_ogona

    # temp = lista[i_min_wartosci]
    # lista[i_min_wartosci] = lista[i_podstawienia]
    # lista[i_podstawienia] = temp

    # albo

    lista[i_min_wartosci], lista[i_podstawienia] = lista[i_podstawienia], lista[i_min_wartosci]
print(lista)

###############################################################################
###############################################################################