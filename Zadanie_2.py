#Zad.2

"""Funkcja do obliczania sześcianu sumy n liczb"""
import datetime
import time

#Pierwszy pomysł
def qube_sum():
    wynik = 0
    number = int(input('Podaj liczbę :'))
    start_time = datetime.datetime.now()
    for x in range(1, number+1):
        wynik += x*x*x
    time_dif = datetime.datetime.now() - start_time
    exec_time = time_dif.total_seconds()
    print(f'Wynik funkcji = {wynik}')
    print(f'Komputer obliczył funkcję w czasie {exec_time}s')

#Pomysł drugi. A raczej pierwszy pomysł(gorszy)
def qube_sum2():
    number = int(input('Podaj liczbę :'))
    lista = []
    start_time = datetime.datetime.now()
    for x in range(1, number+1):
        lista.append(x**3)
    time_dif = datetime.datetime.now() - start_time
    exec_time = time_dif.total_seconds()
    print(f'Wynik funkcji = {sum(lista)}')
    print(f'Komputer obliczył funkcję w czasie {exec_time}s')

# Licznik czasu wykonywania działań

def program_selector(program):

    if program == 1:
        qube_sum()
    elif program == 2:
        qube_sum2()

### After test ... Program 2 zjada potężne ilości pamięci i jest znacznie
# wolniejszy.

prompt1 = "Wybierz który program chcesz użyć (1,2) :"

program = int(input(prompt1))

program_selector(program)

