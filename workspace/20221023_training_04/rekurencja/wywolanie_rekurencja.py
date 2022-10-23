#
# def test_splaszcz(zadanie_rekurencja=None):
#     assert splaszcz([]) == []
#     assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]
#     assert splaszcz([1, 2, 3]) == [1, 2, 3]
#     assert zadanie_rekurencja.splaszcz([1, ]2, 3) == [1, 2, 3]

###########################################################################
###########################################################################

from zadanie_rekurencja import splaszcz

print(dir())


def test_cala_liszta_splaszcz(zadanie_rekurencja=None):
    assert splaszcz([]) == []

def test_cala_liszta_splaszcz(zadanie_rekurencja=None):
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert splaszcz([1, 2, 3]) == [1, 2, 3]
    # assert zadanie_rekurencja.splaszcz([[1, ]2, 3]) == [1, 2, 3]


