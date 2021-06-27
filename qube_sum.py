def program_selector():
    import datetime

    print("Funkcja do obliczania sumy wartości,\nsześcianów kolejnych liczb "
          "naturalnych "
          "aż do wartosci n.")
    """Funkcja do wyboru programu"""
    prompt1 = "Oba programy wynik dają taki sam lecz działają w inny " \
              "sposób.\nCelem testu jest sprawdzenie różnic w czasie " \
              "działania powyższych programów\n\n******  Wybierz który " \
              "program " \
              "chcesz użyć  ****** (1,2) :"
    while True:
        try:
            program = int(input(prompt1))
        except ValueError:
            print('! ! !Podałeś niewłaściwe dane! ! !\nWybierz program '
                  'wpisując 1 '
                  'lub 2\n')
        else:
            break

    if program == 1:
        wynik = 0
        number = int(input('Podaj liczbę :'))
        start_time = datetime.datetime.now()
        for x in range(1, number + 1):
            wynik += x * x * x
        time_dif = datetime.datetime.now() - start_time
        exec_time = time_dif.total_seconds()
        print(f'Wynik funkcji = {wynik}')
        print(f'Komputer obliczył funkcję w czasie {exec_time}s')

    elif program == 2:
        lista = []

        while True:
            try:
                number = int(input('Podaj liczbę :'))
            except ValueError:
                print('Podałeś niewłaściwe dane. Wpisz liczbę naturalną.')
            else:
                break
        start_time2 = datetime.datetime.now()
        for x in range(1, number + 1):
            lista.append(x ** 3)
        time_dif2 = datetime.datetime.now() - start_time2
        exec_time2 = time_dif2.total_seconds()
        print(f'Wynik funkcji = {sum(lista)}\n')
        print(f'Komputer obliczył funkcję w czasie {exec_time2}s')

    else:
        print("Wpisałeś niewłaściwą wartość.\nWybierz program wpisując 1 lub "
              "2")
