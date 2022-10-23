

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
def splaszcz(lista: list) -> list:
    result = []

    for element in lista:
        if type(element) is list:
            for elem_nested in splaszcz(element):
                result.append(elem_nested)
        else:
            result.append(element)
    return result

#
# # splaszcz([1, 2, 3, [4, 5, [6]], 7])
# print(splaszcz([1, 2, 3, [4, 5, [6]], 7]))
