## Zad.4 Given a string, write a Python program that finds all the
# duplicate
##characters which are similar to each others.

#Rozwiązanie
#Na początku importujemy biblioteke string która umozliwi nam utworzenie
# listy wszystkich znaków. Wprowadzanie ręcznie byłoby męczące.

import string

def printing_duplicates():
    """Funkcja do printowania zduplikowanych znaków w inputowanym stringu"""

    #Tworzymy listę wszystkich znaków i zmienną z naszym ciągiem
    dictionary = list(string.printable)
    leter = input("Wpisz ciąg znaków : ")

    #Pętla for iteruję wszystkie znaki naszego stringa i sprawdza czy któryś
    # znak występuje dwa lub więcej razy.
    for digit in dictionary:
        if leter.count(digit) >= 2:
            print(digit)



printing_duplicates()