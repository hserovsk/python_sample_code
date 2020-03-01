import random
SecretNumber = random.randint(1,20)
print('podaj liczbe od 1 do 20')
for guess in range(1,7):
    print('sprobuj odgadnac liczbe.')
    guessnumber = int(input(''))
    if guessnumber < SecretNumber:
        print('Podana liczba jest za mała')
    elif guessnumber > SecretNumber:
        print('Podana liczba jest za duza')
    else:
        break
if guessnumber == SecretNumber:
    print('BRAWO! \n Zgadłeś w ' + str(guess) + ' turze')
else:
    print('niestety nie udało Ci się zgadnąć \n Wylosowana liczba to: ' + str(SecretNumber))
