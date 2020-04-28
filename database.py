import mysql.connector
import sys

print("--------WORKERS DATABASE--------")
user_name = input("enter the login \n")
password = input("enter the password\n")
print("--------------------------------")
try:
    mydb = mysql.connector.connect(host="localhost", user=user_name, passwd=password, database='workers', use_pure=True)
    mycursor = mydb.cursor()
except:
    print("the data provided is incorrect!")
    sys.exit(1)

while True:
    choice = input("Wpisz tresc zapytania sql do bazy danych, \n jesli chcesz zakonczyc program wpisz stop \n jesli chcesz sprawdzic nazwe bazy na ktorej pracujesz wpisz whatbase \n")
    if choice == 'stop':
        print("zakończono prace z baza")
        mycursor.close()
        mydb.close()
        break
    elif choice == 'whatbase':
        print('Nazwa bazy na której aktualnie pracujesz to: ' + name_of_base)
        continue
    elif choice == 'addworker':
        print('Adding worker...')
        name = input('enter the name: ')
        surname = input('enter the surname: ')
        age = int(input('enter the age: '))
        position = input('enter the position: ')
        salary = float(input('enter the salary: '))
        reference = 'Insert into workers (name,surname,age,position,salary) values (%s,%s,%d,%s,%f); ' % (name,surname,age,position,salary)
        mycursor.execute(reference)
        mydb.commit()
    elif choice == 'showall':
        reference = 'select * from workers'
        mycursor.execute(reference)
        result = mycursor.fetchall()
        print('------------------------------------------------')
        print('iD | name | surname | age | position | salary')
        for i in result:
            print(i)
        print('------------------------------------------------')
    else:
        mycursor.execute(reference)
        result = mycursor.fetchall()
        print('------------------------------------------------')
        print('iD | name | surname | age | position | salary')
        for i in result:
            print(i)
        print('------------------------------------------------')


