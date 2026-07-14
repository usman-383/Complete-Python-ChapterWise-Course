class Employee:
    name = "usman"
    Language = "py"
    sallery  = 12000
    Time = 10.5

usman = Employee()
print(usman.name, usman.Language, usman.sallery, usman.Time)





class car:
    name = "usman"
    def __init__(self):
        print(self)
        print("adding new students in database")

s1 = car()
print(s1)



class student:

    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

s1 = student("usman", 90)
print(s1.name, s1.marks)

s2= student("khan", 80)
print(s2.name, s2.marks)


class student:
    college_name = "Hadaf"
    name = "x5"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = student("usman", 90)
print(s1.name, s1.marks)

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val

        print("Hey", self.name, "Your avg marks is", sum/3)

s1 = student("Usman", [12, 14, 16])
s1.get_avg()


class student:

    def __init__(self , name, marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0

        for val in self.marks:
            sum += val

        print("Hey", self.name, "Your avg marks is ", sum/3)

s1 = student("Usman", [2, 4, 6])
s1.get_avg()


class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False

    def started(self):
        self.cluch = True
        self.acc = True
        print("Car Started..........")

c1 = car()
c1.started()



class account:
    def __init__(self, account_num, account_bal):
        self.account_num = account_num
        self.account_bal = account_bal

    def debit(self, ammout):
        self.account_bal -= ammout
        print("Rs",ammout, "Was debit")

    def credit(self, ammount):
        self.account_bal += ammount
        print("Rs", ammount, "Was Credit")

    def get_acc_bal(self):
        return self.get_acc_bal
    
acc1 = account("100", "50")
acc1.credit(100)
acc1.debit(50)

class Account:
    def _int_(self, acc_no, acc_bal):
        self.acc_no = acc_no
        self.acc_bal = acc_bal

    def debit(self, ammount):
        self.acc_bal -= ammount
        print("RS", ammount, "was debited")

    def credit(self, ammount):
        self.acc_bal += ammount
        print("RS", ammount, "was credit")

    def get_acc_bal(self):
        return self.get_acc_bal

acc1 = Account("10000", 500)
acc1.debit(1000)
acc1.credit(500)

class student:
    def __init__(self, name):
        self.name = name 

s1 = student("usman")
print(s1)
print(s1.name)
del s1
