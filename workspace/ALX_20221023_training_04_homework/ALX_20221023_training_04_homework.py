list_01 = ['2', 'a', '5', 'sleep', 254.4, '77', 'cinema', 8787, 9898, 'red']
tuple_01 = ('3', 22, 'blue', '6', 'book', '7867', 'train', 2.2)
set_01 = {'Jake', 66.6, 'John', 876500, 'Eric', 'green', 88, 9}
dictionary_01 = {'age': 65, 'year': 1877, 'books': 176.54, 'pages': 875, 'color': 'purple'}


# new_list = []
# for value in list_01:
#     try:
#         new_list.append(int(value))
#     except ValueError:
#         continue
# lis_sum = sum(new_list)
# print(lis_sum)

########################################################
# def sum_of_digits(my_data):
#     new_list = []
#     for value in my_data:
#         try:
#             new_list.append(int(value))
#         except ValueError:
#             continue
#     lis_sum = sum(new_list)
#     return lis_sum
#
#
# print('=' * 20)
# print(sum_of_digits(list_01), '(sum_of_digits(list_01)')
# print(sum_of_digits(tuple_01), 'sum_of_digits(tuple_01)')
# print(sum_of_digits(set_01), 'print(sum_of_digits(set_01)')
# print('=' * 20)


########################################################
def sum_of_digits(my_data):
    if type(my_data) == list or type(my_data) == set or type(my_data) == tuple:
        new_list = []
        for value in my_data:
            try:
                new_list.append(int(value))
            except ValueError:
                continue
        lis_sum = sum(new_list)
        return lis_sum
    elif type(my_data) == dict:
        new_list = []
        for value in my_data.values():
            try:
                new_list.append(int(value))
            except ValueError:
                continue
        lis_sum = sum(new_list)
        return lis_sum


print('=' * 20)
print(sum_of_digits(list_01), '(sum_of_digits(list_01)')
print(sum_of_digits(tuple_01), 'sum_of_digits(tuple_01)')
print(sum_of_digits(set_01), 'print(sum_of_digits(set_01)')
print(sum_of_digits(dictionary_01), 'print(sum_of_digits(dictionary_01)')
print('=' * 20)

