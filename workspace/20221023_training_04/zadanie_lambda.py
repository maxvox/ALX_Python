from typing import Callable

def przytnij(data: list, start: Callable, stop: Callable) -> list:
    result = []
    czy_dodawac = False
    for element in data:
        if start(element):
            czy_dodawac = True
        if czy_dodawac:
            result.append(element)
        if stop(element):
            break
        return result


print(przytnij(
    data=[1, 2, 3, 4, 5, 6, 7],
    start=lambda x: x % 2 ==0,
    stop=lambda x: x==6,
))