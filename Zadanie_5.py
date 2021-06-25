# Zad.5 Write a Python Program for Linear Search.
# Given an array arr[] of n elements, write a function to search a given element x in
# arr[].

"""Funkcja do wypisywania indexu szukanego elementu w liscie"""
def szukanko():
    #Tworze dowolną liste liczb

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

szukanko()