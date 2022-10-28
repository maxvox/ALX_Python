## Pętle

# Pętla while

# pętla nieskończona i skończona
# while True:
#     print()


#### wersja 1
# i = 0
# while True:
#     print("działam")
#     i += 1
#     if i == 7:
#         break


#### wersja 2
# i = 0
# while i<7:
#     print("działam")
#     i += 1

# while (i := 0)<7:
#     print("działam")
#     i += 1


# i=5
# while i<7:
#     if i ==5:
#         i += 1
#         continue
#     print(i)

#
# i = 0
# while i <7:
#     print(i)
#     i +=1
#     if i == 3:
#         break
# else:
#     print("zakonczone")

# i=1
# while i <101:
#     print(i**2)
#     i+=1
# else:
#     print("done")


# while input_int <= 4:
#     input_int = int(input("podaj liczbę lub k aby zakończyć "))
#     if input_int
#     print((input_int + input_int) / 2)
#     if input_int == "k":
#         break
# else:
#     print("Wartość nieznana")

################################################################
################################################################


# suma_liczb = 0
# ilosc_zapytan = 0
#
# max_number = 0
# min_mumber = 0
#
# while True:
#     input_int = input("podaj liczbę lub k aby zakończyć ")
#
#     if input_int == "k":
#         break
#
#     input_int = int(input_int)
#     suma_liczb = suma_liczb + input_int
#     ilosc_zapytan += 1
#
#     if max_number is None or input_int > max_number:
#         max_number = input_int
#
#     if min_mumber is None or input_int < min_mumber:
#         min_mumber = input_int
#
# print("średnia wynosi", suma_liczb/ilosc_zapytan)
# print("Max ", max_number)
# print("Min ", min_mumber)

################################################################
################################################################

# print() co drugą liczbę do 100

# krok = 1
# while krok <= 100:
#     print(krok)
#
#     krok +=2

################################################################
################################################################

# i = 1
# while i <= 100:
#     if i % 7 ==0:
#         print(i)
#     i +=1

################################################################
################################################################

# napis = "Ala ma kota"    # niemutowalny
# print(len(napis))
# print ("A" in napis)
#
# print(napis.lower().count("a"))
# print(napis.index("A"))
#
# print(napis[10])
# print(napis[10] + napis[6] + napis[2])
# print(napis[3:6])
# print(napis[1:10:2])
# ### print(napis[1<--------od znaku:10<-------do znaku:2<---------co drugi znak])
# print(napis[:6])
# print(napis[6:])
# print(napis[-6:])
# print(napis[:3:6])
# print(napis[::6])
# print(napis[::-1]) # odwrócony napis   atok am alA
#
#
# napis2 = "88" + napis[2:]
# print(napis2)     # ----> 88a ma kota


################################################################
################################################################


# Tuple / Krotka          # niemutowalny
### index
###  count


# t = (1, 3, 1, 4, 3, 2, "a", "hj")
# print(t.count(2))
# print(t.index(2, 3))

# print(help(t.index))
# print(t[1::-2])

### t[0]= 10

# print(tuple("123"))
# print(tuple)
# print(type(1,))


################################################################
################################################################

### lista    # typ mutowalny

# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# METRODY do przetestowania
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# l = [2, 4, 2,5 , 5, "ghj", "ii", "UI"]
# k = [2, 4, 2,5 , 5]


# print(dir(l))
# print("1", k.sort())  # <------------- jeśli lista zawiera zame liczby/cyfry
# print("0", sorted(k))  # <------------- jeśli lista zawiera zame liczby/cyfry


# a = [1, 2, 3]
# b = a.copy()   # shallow copy
# b.append(5)

# print(2, a, b)


# a = [1, 2, 3]
# a = [1, 2, a]
# print('000', b)

# c = b.copy()
# a.append(4)
# print('6654', b, c)

# import copy
# c = copy.deepcopy(b)
# a.append(4)
# print('0098', b, c)


# print(help(l.clear()))


# METRODY do przetestowania
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# d = {}
# print(dir(d))
# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']



# Pętle FOR

# dane = [1,2,3,4,3,2,4,6,7,2.8888888888888888888, "x"]
#
# szukane = 2
# licznik_wyszukania = 0
# for element in dane:
#     if element == szukane:
#         licznik_wyszukania += 1
# print(element)

### zadanie
"""
1. utwórz tuplę 10 elementow
wyświetl elementy:
- 2go
- przedostatni
- od 3go do 7go włącznie
- co trzeci
- odwróć kolejność tupli

2. utwórz napis i powtórz te kroki powyższe

3. Utwórz listę 10 elem.
- dołącz element do listy
- wsadz nowy element przed 3 indexem
- zmien wartosc na indeksie 5
- zrzuć ostatnią wartość (pop)
"""

# ZAD1
# tuple_1 = (1, 4, 2,5 ,26, 4, 2, 9, "a", "po", "re")
# print('tupla, element 1szy: ', tuple_1[0])
# print('tupla, element przedostatni: ', tuple_1[-2])
# print('tupla, element od 3 do 7 włącznie: ', tuple_1[2:7])
# print('tupla, element co 3ci: ', tuple_1[0::3])
# print('tupla, elementy odwrócone: ', tuple_1[::-1])

# ZAD2
# napis = "1, 4, 2,5 ,26, 4, 2, 9, a, po, re"
# print('napis, element 1szy: ', napis[0])
# print('napis, element przedostatni: ', napis[-2])   # TBD
# print('napis, element od 3 do 7 włącznie: ', napis[2:7])
# print('napis, element co 3ci: ', napis[0::3])
# print('napis, elementy odwrócone: ', napis[::-1])

# # ZAD3
# lista = [1, 4, 2,5 ,26, 4, 2, 9, "a", "po", "re"]
#
# lista.append(5)
# print('dołącz element do listy', lista)
#
# lista  # tbd
# print('wsadz nowy element przed 3 indexem', lista)   # tbd
#
#
# print('zmien wartosc na indeksie 5', lista)   # tbd
#
#
# print('zrzuć ostatnią wartość (pop)', lista)   # tbd


# Napisz program obliczajacy srednia wartosc z podanych przez uzytkownika liczb
# uzyj listy, skorzystaj z funkcji: sum, len, min, max
#
# x = []
#
# x = list()






# lista_liczb = [-20.44, 20, -66, -76, -789, -44, 67, 90, 79, 56]
# print(sum(lista_liczb))
#
# dodatnich = 0
# ujemnych = 0
#
# for element in lista_liczb:
#         if element > 0:
#             dodatnich +=1
#         elif element< 0:
#             ujemnych+=1
#
# print(f'{dodatnich} {ujemnych}')


###############################################################################
###############################################################################

# x = "ala ma kota kot ma ale "
# y = "ala ma kota kot ma ale "
#
# print(x==y)

###############################################################################
###############################################################################

# idiomy, wyrażenia listowe, generatorowe
# przykład idiomu pythonowego

# x = [1, 2, 5, 2, 1, 7]
#
# szesciany = []
# for element in x:
#     szesciany.append(element**3)
#
# szesciany2 = [element ** 3 for element in x]
#
#
# szesciany_liczb_parzystych = []
# for element in x:
#     if element % 2 -- 0:
#         szesciany_liczb_parzystych.append(element**3)
#
# szesciany_liczb_parzystych = [element ** 3 for element in x if element % 2 ==0]
#
# szesciany2 = [element** 3 for element in x]
# print(szesciany2)
#
# for element in szesciany2: print(element)

###############################################################################
###############################################################################

#
# for y in range(1,11):
#     for x in range(1,11):
#          print ("   |",x*y, end="|")
#     print()
#     print(75*"_")
#     print()



############ versja -0-

# print(60*"-")
# for y in range(0,11):
#     for x in range(0,11):
#         print (f" {x*y:>3}" , end="|")
#     print()
# print(60*"-")



############ versja -1-

# print('', end='     ')
# for i in range(10):
#     print(f'{i:3}', end=' ')
# print()
# print()
# for i in range(10):
#     print(i, end='     ')
#     for j in range(10):
#         print(f'{i * j:3}', end=' ')
#     print()



###############################################################################
###############################################################################

