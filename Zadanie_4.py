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
        if leter.count(digit) > 1:
            print(digit)

printing_duplicates()


# Pomysł drugi po doedukowaniu się w internecie. Output wpada do słownika

def printing_duplicates2():
    text = input('Wpisz ciąg znaków :')
    duplicates = set()
    for digit in text:
      if text.count(digit) > 1:
        duplicates.add(digit)
    print(duplicates)

printing_duplicates2()