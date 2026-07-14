#OOP IN PYTHON:
          # To map with real world scenarios, we started  using objects in code.

#CLASS AND OBJECTS IN PYTHON:

#CLASS :-> Class is a blue print for creting object.


class student:
    name = "usman"

s1 = student()
print(s1.name)
         

         #Or

class car:
    colour = "black"
    brand = "BMW"

car1 = car()
print(car1.colour)
print(car1.brand)


#_ _ _int_ _ _ Function

#Connstructor :-> All classes have a function called _int_ (), which is always axecuted when the class in being initiated.

class car:
    name = "usman"

    def __init__(self):
        print(self)
        print("adding new students in database")

s1 = car()
print(s1)


class student:

    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in database")

s1 = student("usman", 90)
print(s1.name, s1.marks)

s2= student("khan", 80)
print(s2.name, s2.marks)

#DEFAULT CONSTRUCTOR:-> which has only self parameter.
#PARAMETERIZEZ CONSTRUCTOR:-> whixh has parameter other than self

class student:
    collecge_name = "HADAF"
    name = "any"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database")

s1 = student("usman", 97)
print(s1.name, s1.marks)

s2 = student("khan", 80)
print(s2.name, s2.marks)

#CLASS AND INTANCE ATTRIBUTES:

 
 #METHODS:
          #Methods are function that belong to objects.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hey", self.name, "your avg marks is", sum/3)

s1 = student("usman", [90 ,80, 100])
s1.get_avg()


#STATIC METHD:
             #Static method that dont  use the self parameter(work at class lvl)

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hey", self.name, "your avg marks is", sum/3)

s1 = student("usman", [90 ,80, 100])
s1.get_avg()
s1.hello()


#ABSTRACTION:
            #Hiding the implementation details of a class and only showing the essential feature to the user.

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False
    
    def started(self):
        self.cluch = True
        self.acc = True
        self.brk = True
        print("car started")

car1 = car()
car1.started()


#ENCAPSULATION:
             #Wrapping data and functions into a single unit(object)

#Practice question:
                  #Create account class with 2 attributes balance and account no.create method for debit, credit and printing the balance

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

acc1 = Account("10000", "5")
acc1.debit(1000)
acc1.credit(500)
