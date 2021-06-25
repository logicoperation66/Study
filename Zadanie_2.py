#Zad.2

"""Funkcja do obliczania sześcianu sumy n liczb"""


def qube_sum():
    wynik = 0
    number = int(input('Podaj liczbę :'))
    for x in range(1, number+1):
        wynik += x*x*x
    print(wynik)

qube_sum()