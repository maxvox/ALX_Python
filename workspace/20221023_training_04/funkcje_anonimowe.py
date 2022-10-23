def second(x):
    return x[1]


sec = lambda x: x[1]
sec.__name__ = 'sec'

print(second, sec)  #  <function second at 0x7ff58dfe6dc0> <function <lambda> at 0x7ff58dfe7160>
print(second.__name__, sec.__name__)  # second sec

lista = ['a5', 'c0', 'b1']
print(sorted(lista, key=second))   #  ['c0', 'b1', 'a5']
print(sorted(lista, key=sec))   #  ['c0', 'b1', 'a5']
print(sorted(lista, key=lambda x: [1]))   #  ['a5', 'c0', 'b1']

zmienna = lambda x, y: print(x + y)
print(zmienna, '>>>__zmienna')   #<function <lambda> at 0x7fa5ccc7a940> >>>__zmienna


(lambda x, y: print(x + y))(1, 4)   #  5
