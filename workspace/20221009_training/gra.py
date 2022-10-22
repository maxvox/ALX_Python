import random

print(__debug__)
print(__name__)
DEBUG = True

gracz_x = 5
gracz_y = 9

skarb_x = 5
skarb_y = 8

ruch_counter = 0

odleglosc_pocz = abs(gracz_x-skarb_x) + abs(gracz_y-skarb_y)

while True:
    odleglosc_pocz = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    polecenie = input("Wykonaj ruch (w-gora, a-lewo, s-col, d-prawo)")

    # if polecenie == "w" or polecenie == "s" or polecenie == "a" or polecenie == "d":
    #     ruch_counter += 1

    if polecenie in "wasd" and len(polecenie)==1:
        ruch_counter += 1



    if polecenie == "k": break
    if polecenie == "w":
        gracz_y += 1
    elif polecenie == "s":
        gracz_y -= 1
    elif polecenie =="a":
        gracz_x -= 1
    elif polecenie == "d":
        gracz_x +=1
    else:
        print("nie wiem gdzie isc")

    odleglosc_po = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    if odleglosc_po < odleglosc_pocz:
        print("cieplo")
    elif odleglosc_po > odleglosc_pocz:
        print("zimno")

if DEBUG:
    print(f'Pozycja gracza: {gracz_x} {gracz_y}')
    print(f'Pozycja skarbu: {skarb_x} {skarb_y}')

    if gracz_y == skarb_y and gracz_x == skarb_x:
        print("wygrales")
        break

    if gracz_y > 10:
        print("wypadłeś")
        break
