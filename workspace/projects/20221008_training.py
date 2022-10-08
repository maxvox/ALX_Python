# produkt_1 = "pomidory"
# waga_1 = 12.87
# cena_1 = 22.34
# suma_1 = waga_1*cena_1
#
# produkt_2 = "ogórki"
# waga_2 = 34.11
# cena_2 = 2.33
# suma_2 = waga_2*cena_2
#
#
# produkt_3 = "śmietana"
# waga_3 = 12.22
# cena_3 = 32.22
# suma_3 = waga_3*cena_3
#
# pomidory_suma = f'{produkt_1:20} {suma_1:6.2f} PLN'
# ogorki_suma = f'{produkt_2:20} {suma_2:6.2f} PLN'
# smietana_suma = f'{produkt_3:20} {suma_3:6.2f} PLN'
# suma = suma_1 + suma_2 + suma_3
#
#
#
# print(pomidory_suma)
# print(ogorki_suma)
# print(smietana_suma)
# print(suma)
#
# raport =f"""
# {produkt_1:20} {waga_1:6} kg {cena_1:6} PLN
# {produkt_2:20} {waga_2:6} kg {cena_2:6} PLN
# {produkt_3:20} {waga_3:6} kg {cena_3:6} PLN
# {'-'*40}
# {'suma:':20}{'':8}{suma:5.2f} PLN
# """
# print(raport)

###################################################################################################################

# for i in range(10): {print(i)}
# for i in range(10):
#     print(i)

###################################################################################################################

"""Napisz program, który pobierze od użytkownika dane i wyliczy jego współczynnik BMI
"""

# waga = float(input("Podaj swoją wagę w kg: "))
# wzrost = float(input("Podaj swój wzrost w cm: "))
# wzrost_cm = wzrost/100
# BMI = waga/((wzrost_cm)**2)
#
# print(f"{BMI:.2f}")

###################################################################################################################
# nazwa = "lskjakdasjdiasjdks saodjaskldnasid asdjasjdlkasjd"
# nazwa_2 = "lskjakdasjdiasjdks saodjaskldnasid "
#
# len_nazwa = len(nazwa)
#
# print(f"""
# {nazwa:{len_nazwa}} X
# {nazwa_2:{len_nazwa}} X
# """)

###################################################################################################################

### Zadanie

### Napisz program, który obliczy koszty przejazdu z miasta A do B


### Miasto: Warszawa
### Miasto B: Gdańsk

# dystans_Warszawa_Gdansk = 420
# cena_paliwa = 7.25
# spalanie_na100km = 10

### Koszt przejazdu Warszawa-Gdańsk to 304.50 PLN


# przejazd = "Koszt przejazdu Warszawa-Gdańsk to "
# litry = dystans_Warszawa_Gdansk*spalanie_na100km/100
# suma = (litry*cena_paliwa)
#
# print(f'{przejazd}{suma}')

###################################################################################################################

# current_year = 2022
# b_year = int(input("Podaj rok urodzenia: "))
#
#
# if current_year - b_year >= 18:
#     print("Użytkownik pełnoletni.")
# else:
#     print("Użytkownik nie jest pełnoletni.")

###################################################################################################################

# pierwsza_liczba = int(input("Podaj pierwszą liczbę: "))
# druga_liczba = int(input("Podaj drugą liczbę: "))
# operator = input("Podaj rodzaj operacji: ")
#
#
# if operator == "+":
#     result = pierwsza_liczba + druga_liczba
# elif operator == "-":
#     result = pierwsza_liczba - druga_liczba
# elif operator == "*":
#     result = pierwsza_liczba * druga_liczba
# elif operator == "/":
#     if druga_liczba == 0:
#         result = "Pamiętaj cholero nie dzielić przez zero!"
#     else:
#         result = pierwsza_liczba / druga_liczba
# elif operator == "**":
#     result = pierwsza_liczba ** druga_liczba
# else:
#     result = "Nieznana operacja"
# print(result)

# print(f'{pierwsza_liczba} {operator} {druga_liczba}')


###################################################################################################################

lokalizacja_1 = int(input("Wpisz wartość pierwszą, gdzie się znajdujesz? "))
lokalizacja_2 = int(input("Wpisz wartość drugą, gdzie się znajdujesz? "))

print(lokalizacja_1, lokalizacja_2)
result = ''

if lokalizacja_1 >= 0 or lokalizacja_1 <=10 and lokalizacja_2 >=0 or lokalizacja_2 <=10:
    result = "Jesteś w lewym dolnym rogu."
elif lokalizacja_1 >100 or lokalizacja_1 <0 and  lokalizacja_2 >100 or lokalizacja_1 <0:
    result = "Jesteś poza planszą"
elif lokalizacja_1 >= 90 or lokalizacja_1 <=100 and lokalizacja_2 >=0 or lokalizacja_2 <=10:
    result = "Jesteś w lewym górnym rogu."
elif lokalizacja_1 >= 90 or lokalizacja_1 <=100 and lokalizacja_2 >=90 or lokalizacja_2 <=100:
    result = "Jesteś w prawym górnym rogu."
elif lokalizacja_1 >= 0 or lokalizacja_1 <=10 and lokalizacja_2 >=0 or lokalizacja_2 <=10:
    result = "Jesteś w prawym dolnym rogu."
elif lokalizacja_1 >= 10 or lokalizacja_1 <=90 and lokalizacja_2 >=0 or lokalizacja_2 <=10:
    result = "Jesteś w lewym pasku rogu."
elif lokalizacja_1 >= 90 or lokalizacja_1 <=100 and lokalizacja_2 >=0 or lokalizacja_2 <=10:
    result = "Jesteś w prawym górnym rogu."
elif lokalizacja_1 >= 90 or lokalizacja_1 <=100 and lokalizacja_2 >=0 or lokalizacja_2 <=10:
     result = "Jesteś w prawym górnym rogu."
else:
    result = "Jesteś w centrum"




print(result)



# dp >= 0.0 and dp >= 10.10
# dl =
#
# gl =
# gp =



































