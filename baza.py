import mysql.connector
import sys

print("--------BAZA-DANYCH-PRACOWNIKOW--------")
user_name = input("Podaj login \n")
password = input("Podaj hasło\n")
name_of_base = input("Podaj nazwe bazy na której chcesz pracowac\n")
try:
    mydb = mysql.connector.connect(host="localhost", user=user_name, passwd=password, database=name_of_base, use_pure=True)
    mycursor = mydb.cursor()
except:
    print("podane dane są nieprawidłowe ")
    sys.exit(1)

while True:
    reference = input("Wpisz tresc zapytania sql do bazy danych, \n jesli chcesz zakonczyc program wpisz stop \n jesli chcesz sprawdzic nazwe bazy na ktorej pracujesz wpisz whatbase \n")
    if reference == 'stop':
        print("zakończono prace z baza")
        mycursor.close()
        mydb.close()
        break
    elif reference == 'whatbase':
        print('Nazwa bazy na której aktualnie pracujesz to: ' + name_of_base)
        continue
    else:
        mycursor.execute(reference)
        result = mycursor.fetchall()
        for i in result:
            print(i)


