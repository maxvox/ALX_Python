from ALX_20221023_training_04_homework import sum_of_digits, tuple_01, list_01, set_01, dictionary_01


def test_sum_of_digits():
    # Checking if the sum of the digits in list_01 is equal to 19023.
    assert sum_of_digits(list_01) == 19023
    # Checking if the sum of the digits in tuple_01 is equal to 7900.
    assert sum_of_digits(tuple_01) == 7900
    # Checking if the sum of the digits in set_01 is equal to 876663.
    assert sum_of_digits(set_01) == 876663
    # Checking if the sum of the digits in dictionary_01 is equal to 2993.
    assert sum_of_digits(dictionary_01) == 2993
    assert sum_of_digits((1, 2, 3)) == 6

# def test_sum_sum_of_digits():
#
