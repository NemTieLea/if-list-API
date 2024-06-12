# import random

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kwadraty_liczby = []

for liczba in liczby:
    kwadraty_liczby.append(liczba ** 2)

# print(kwadraty_liczby)

kwadraty_liczby_2 = [liczba**2 for liczba in liczby]
# print(kwadraty_liczby_2)

# [<zmienna> for <zmienna> in <iterowalny_obiekt(np. lista)>]

# imiona = ["adam", "Ewa", "Wojtek", "Robert", "marcin", "michal"]
# imiona_2 = [imie.capitalize() for imie in imiona]
# imiona_3 = [imie.upper() for imie in imiona]
#
# print(imiona)
# print(imiona_2)
# print(imiona_3)
#
# print(f"Dobrze wprowadzone imiona (brak wielkiej litery na poczatku): {sum(imiona_2)} / {len(imiona)}")

imiona = ["adam", "Ewa", "Wojtek", "Robert", "marcin", "michal"]
imiona_warning = [i for i in imiona if not i.istitle()]

# [<zmienna> for <zmienna> in <iterowalny_obiekt(np. lista)> if <warunek>]

# print(f"Imiona zle zapisany: {imiona_warning}")

# wybierz losowe ok 20% firm do kontroli

# do_kontroli = [i for i in imiona if random.random() > 0.8]
# print(f"Osoby do kontroli: {do_kontroli}")
#
# liczby = [liczba for liczba in range(10)]
# print(liczby)
# litery = [(index, litera.upper()) for index, litera in enumerate("WGR 10A01")]
# print(litery)

dni_pogoda = [
    ("Poniedzialek", 18),
    ("Wtorek", 21.5),
    ("Sroda", 24.9),
    ("Czwartek", 17.8),
    ("Piatek", 12.1),
    ("Sobota", 18),
    ("Niedziela", 28.7)
]


def co_ubrac(temperatura):
    return "kurtka" if temperatura < 21 else "kapelusz"


dni_ubranie = [
    (dzien, co_ubrac(temp))
    for dzien, temp in dni_pogoda
    if dzien in ["Poniedzialek", "Wtorek", "Sroda"]
]

# print(dni_ubranie)

# [1, 2, 3, 4, 5, 6, 7, 8, 9,]
lista_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
lista_1d = [a for b in lista_2d for a in b]
# print(lista_1d)

imiona = ["adam", "Ewa", "Wojtek", "Robert", "marcin", "michal"]

imiona_slownik = {imie: len(imie) for imie in imiona}
# print(imiona_slownik)

# {<klucz>: <wartosc> for <element> in <iterowalny_obiekt>}

imiona_indeksowane = {idx: imie.capitalize() for idx, imie in enumerate(imiona, start=1)}
# print(imiona_indeksowane)

imiona_miasta = {
    'Wojtek': "Warszawa",
    'Robert': "Poznan",
    'Marcin': "Poznan",
    'Michal': "Gdansk",
}

osoby_z_poznania = {
    imie: miasto
    for imie, miasto in imiona_miasta.items()
    if miasto == "Poznan"
}
print(osoby_z_poznania)
