def add(a, b, *args, c=1, d=2, **kwargs):
    print(kwargs, 'kwargs')   # create dictionary
    print(args, type(args), '001')
    return a + b + sum(args)


add(1, 3)
add(12, 3, 4, 4, 3, 2, 1, 8)

a, b, *c = 1, 2, 4, 2, 5, 4, 8
print(a, b, c, '002')

lista = [12, 3, 4, 4, 3, 2, 1, 8]
print(a, b, c, '003')
add(10, 20, *[1, 3, 5, 8])
add(10, 20, *lista)
add(1, 2, 3, 4, 5, 6, 7, e=44, f=66)


def hello(name='Ada', age=22) -> [str, int]:
    print(name, age)


print('Kasia', 77)
#### dwie gwiazdki -> słownik  -> **kwargs

