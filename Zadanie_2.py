#Zad.2

"""Funkcja do obliczania sześcianu sumy n liczb"""

number = int(input('Podaj liczbę :'))
wynik = 0

for x in range(1, number+1):
    wynik += x*x*x
print(wynik)

