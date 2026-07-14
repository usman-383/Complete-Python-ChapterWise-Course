#INHERITANCE:
            #When one class (child/derived) derives the properties and method of another class(parent/base)

class Car:
    colour = "black"

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped.")

class Toyotacar(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("supra")

print(car1.name)
print(car1.colour)

print(car2.name)
print(car2.colour)

#TYPES OF INHERITANCE:

#1)SINGLE INHERITANCE:

class Car:
    colour = "black"

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped.")

class Toyotacar(Car):
    def __init__(self, name):
        self.name = name

print(car1.name)
print(car1.colour)

print(car2.name)
print(car2.colour)

#2)MULTI-LVL INHERITANCE


class Car:
    colour = "black"

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped.")

class Toyotacar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(Toyotacar):
    def __init__(self, type):
        self.type = type


car1 =Fortuner("disel")
car1.start()



#3)MULTIPLE INHERITANCE:

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

C1 = C()

print(C1.varA)
print(C1.varB)
print(C1.varC)