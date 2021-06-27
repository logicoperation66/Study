# Zad.5 Write a Python Program for Linear Search.
# Given an array arr[] of n elements, write a function to search a given element x in
# arr[].

"""Funkcja do wypisywania indexu szukanego elementu w liscie"""
import random

def list_randomizer(min,max,much):
    '''Funkcja do tworzenia listy losowych liczb'''
    result_list = []

    while len(result_list) < much:
        result_list.append(random.randrange(min,max))
    return result_list

def szukanko():
    '''Funkcja do szukania wśród listy losowych liczb'''

    lista = [10,11,13,16,17,95,45,68,48,33,51,47,]
    szukana = int(input('Podaj jakiej liczby szukasz :'))

    #lista = list(set(lista))

    print(f'Twoja lista wygląda następująco {lista}')
    print(f"Szukamy elementu [{szukana}]")
    for element in lista:
        if szukana == element:
            print(f"{szukana} znajduję się na liście pod indexem "
                  f"{lista.index(szukana)}")
            break
    else:
        print(f'Szukanej {szukana} nie ma na liście.')

#rand_list = list_creator(int(input('min :')),int(input('max :')),int(input(
#    'how much :')))

def list_maker():#                 !!!!Do dokończenia w wolnej chwili...!!!
    ##Funkcja do tworzenia listy. Dokończyć
    result_list = []

    while True:
        value = input('Wpisz liczbę którą chcesz dodać. Jeśli chcesz '
                           'zakończyć, nie wpisuj nic :')
        simple_intiger = int()
        if value == '':
            print('Koniec tworzenia listy.')
            print(f'Oto twoja lista \n{result_list}')
            return result_list
        else:
            result_list.append(int((value)))
            print(result_list)
            continue

list_maker()
