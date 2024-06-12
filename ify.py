"""
skrotowe operacje: iterowanie po listach, slownikach
skrotowa operacja "if
"""

temperatura = 24.5
pada_deszcz = True
if temperatura > 22 and not pada_deszcz:
    komunikat = "nie trzeba zakladac kurtki"
else:
    komunikat = "trzeba zalozyc kurtke"
# print(komunikat)

komunikat_2 = "nie trzeba zakladac kurtki" if temperatura > 22 and not pada_deszcz else "trzeba zalozyc kurtke"
# print(komunikat_2)

# zmienna = <wartosc_jesli_prawa> if <warunek> else <wartosc_jesli_nieprawda>

# ======================================================== #

wiek = 19
obywatelstwo = "polskie"
miejsce_zamieszkania = "Warszawa"
ma_wazny_dowod = True
godzina = "16:00"
if (
    wiek >= 18
    and obywatelstwo == "polskie"
    and miejsce_zamieszkania == "Warszawa"
    and ma_wazny_dowod
    and "08:00" <= godzina <= "22:00"
):
    moze_glosowac = True
else:
    moze_glosowac = False


def ocen_czy_moze_glosowac(wiek, obywatelstwo, ma_wazny_dowod, godzina):
    return (
        wiek >= 18
        and obywatelstwo == "polskie"
        and miejsce_zamieszkania == "Warszawa"
        and ma_wazny_dowod
        and "08:00" <= godzina <= "22:00"

    )


moze_glosowac = ocen_czy_moze_glosowac(wiek, obywatelstwo, ma_wazny_dowod, godzina)
