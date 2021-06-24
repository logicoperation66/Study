#Zad.2

"""Funkcja do obliczania sześcianu sumy n liczb"""

number = int(input('Podaj liczbę :'))
summ = []

for x in range(1, number+1):
    qube = x**3
    summ.append(qube)
wynik = sum(summ)
print(wynik)
## To jest jakaś abstrakcja... ale to pierwszy pomysł jaki mi wpadł głowy...
# DO POPRAWY
