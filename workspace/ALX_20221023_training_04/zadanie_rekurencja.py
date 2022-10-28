"""

Zaimplementuj funkcję spłaszczającą podaną listę.
Przykład użycia:

>>> splaszcz([1, 2, 3, [4, 5, [6]], 7])
[1, 2, 3, 4, 5, 6, 7]

"""


# def splaszcz(jakies_dane):
#     lista = []
#     # print(type(lista)) # <class 'list'>
#     jakies_dane = ([1, 2, 3, [4, 5, [6]], 7])
#     # print(type(jakies_dane)) # <class 'list'>
#
#     for dane in jakies_dane:
#         lista = (lista.append(dane))
#         return lista
#         print(type(lista))
#         print(lista)

# jakies_dane = ([1, 2, 3, [4, 5, [6]], 7])
# for dane in jakies_dane:
#     print(" ".join(map(str, dane))

### ver -1-  ->> OK

# def splaszcz(lista: list) -> list:
#     result = []
#     for element in lista:
#         if type(element) is not list:
#             result.append(element)
#         else:
#             for elem_nested in splaszcz(element):
#                 result.append(elem_nested)
#
#     return result
#
# splaszcz([1, 2, 3, [4, 5, [6]], 7])
###########################################################################
###########################################################################

#### ver -2-  ->> OK
# def splaszcz(lista: list) -> list:
#     result = []
#
#     for element in lista:
#         if type(element) is list:
#             for elem_nested in splaszcz(element):
#                 result.append(elem_nested)
#         else:
#             result.append(element)
#     return result
#
#
# # splaszcz([1, 2, 3, [4, 5, [6]], 7])
# print(splaszcz([1, 2, 3, [4, 5, [6]], 7]))

###########################################################################
###########################################################################

# ys = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
# for xs in ys:
#     print(" ".join(map(str, xs)))
###########################################################################
###########################################################################

# A = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
# def x()->int:
#     for i in A:
#             print(*i)
#
# print(x())   #  None
###########################################################################
###########################################################################











