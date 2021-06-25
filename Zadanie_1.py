# Zad. 1 Program do obliczania podatku.

"""Prosta aplikacja do liczenia należnego podatku z funkcją sprawdzania
poprawności wprowadzonych danych"""


def tax():
    pr1 = 3091
    pr2 = 85528
    st1 = 0.18
    st2 = 0.32

    prompt1 = "Podaj jaki masz dochód"

    print(prompt1)
    while True:
        try:
            bejmy = float(input('zł :'))
        except ValueError:
            print('Podałeś niewłaściwe dane. Wpisz kwote.')
        else:
            break

    if pr1 < bejmy < pr2:
        ciezar = st1*(bejmy-pr1)
        print(f"Musisz odprowadzić {round(ciezar, 2)} zł podatku")
    elif bejmy > pr2:
        ciezar2 = st1*(pr2-pr1)+st2*(bejmy-pr2)
        print(f"Musisz odprowadzić {round(ciezar2, 2)} zł podatku")
    else:
        print('Jesteś zwolniony z podatku "szczęsciarzu"')


tax()