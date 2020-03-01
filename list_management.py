lista = []
true = 1
def progr():
    print('Witaj w programie do tworzenia list \n wpisz łańuch znaków który chcesz dodać \n aby zobaczyc liste wpisz pokaz \n aby usnac element z listy wpisz usun \n')
    while true:
        word = input('podaj łańcuch \n')
        if word == 'stop':
            print(lista)
            break
        elif word == 'usun':
            wybor = int(input('podaj ktory element listy chcesz usunac \n'))
            lista.pop(wybor)
        elif word == 'pokaz':
            print(lista)
        else:
            lista.append(word)
progr()