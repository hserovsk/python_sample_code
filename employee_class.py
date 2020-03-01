class employee:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        self.bonus = 0
    def setbonus(self,all_day_work=0,day_in=0):
        presence_at_work = (all_day_work / day_in)
        if presence_at_work > 1 and presence_at_work < 1.10:
            self.bonus = self.bonus + (presence_at_work*750)
        elif presence_at_work  > 1.10 and presence_at_work < 1.20:
            self.bonus = self.bonus + (presence_at_work*250)
        elif presence_at_work > 1.20:
            pass
        else:
            print("podano bledna wartosc")
    def setsalary(self,money):
        self.salary = money + self.bonus
    def info(self):
        print("------EMPLOYEE------")
        print(" Name: %s \n Surname: %s \n Age: %d " % (self.name,self.surname,self.age))
        print(" Salary with bonus: %.2f zł" % self.salary)
hubert = employee('Hubert','Serowski',22)
hubert.setbonus(200,185)
hubert.setsalary(3000)
hubert.info()
monika = employee('Monika','Janicka',30)
monika.setbonus(200,168)
monika.setsalary(4000)
monika.info()