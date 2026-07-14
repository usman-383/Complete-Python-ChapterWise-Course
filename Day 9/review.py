# class student:
#     def __init__(self,name):
#         self.name = name
# s1 = student("usman")
# print(s1)
# print(s1.name)
# del s1.name


# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass

# acc1 = Account("usman", "549")
# acc2 = Account("khan", "x5")

# print(acc1.acc_no, acc1.acc_pass)
# print(acc2.acc_no, acc2.acc_pass)


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("1234", "abcd")
# print(acc1.acc_no)
# print(acc1.reset_pass())


# class car:
#     colour = "black"

#     @staticmethod
#     def start():
#         print("car started.....")

#     @staticmethod
#     def stop():
#         print("car stoped......")

# class ToyotaCar(car):
#     def __init__(self,name):
#         self.name = name
    
# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("supra")

# print(car1.name)
# print(car1.colour)

# print(car2.colour)
# print(car2.name)


#1
# class car:
#     colour = "black"

#     @staticmethod
#     def start():
#         print("car started.....")

#     @staticmethod
#     def stop():
#         print("car stoped......")

# class ToyotaCar(car):
#     def __init__(self,name):
#         self.name = name
    
# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("supra")

# print(car1.name)
# print(car1.colour)

# print(car2.colour)
# print(car2.name)


#2
# class car:
#     colour = "black"

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stoped...")

# class Toyotacar(car):
#     def _init_ (self,brand):
#         self.brand = brand

# class Fortuner(Toyotacar):
#     def _init_(self,type):
#         self.type = type

# car1 = Fortuner("Diesel")
# car1.start()


# #3
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# C1 = C()

# print(C1.varA)
# print(C1.varB)
# print(C1.varC)


#super method

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stoped.")
        
# class Toyotacar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)

# car1 = Toyotacar("prius", "electric")
# print(car1.type)



#cass method
# class person:
#     name = "usman"

#     def changename(self,name):
#         person.name = name

# p1 = person()
# p1.changename("khan")
# print(p1.name)
# print(person.name)


# class person:
#     name = "usman"

#     @classmethod
#     def changename(cls,name):
#         cls.name = name

# p1 = person()
# p1.changename("khan")
# print(p1.name)
# print(person.name)



# class student:
#     def __init__(self,che,phy,bio):
#         self.che = che
#         self.phy = phy
#         self.bio = bio
#         self.percrntage = str((self.che + self.phy + self.bio)/3) + "%"

# st1 = student(80,90,100)
# print(st1.percrntage)


# class student:
#     def __init__(self,che,phy,bio):
#         self.che = che
#         self.phy = phy
#         self.bio = bio

#     @property
#     def percentage(self):
#         return str((self.bio + self.che + self.phy)/3) + "%"
    
# st1 = student(90,80,100)
# print(st1.percentage)

# # st1.phy=(130)
# # print(st1.percentage)


# class complex:
#     def _init_(self,real,img):
#         self.real = real
#         self.img = img

#     def shownum(self):
#         print(self.real,"i +", self.img,"y")

#     def add(self,num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return complex(newreal,newimg)

# num1 = complex(1,3)
# num1.shownum()

# num2 = complex(2,2)
# num2.shownum()

# num3 = num1.add(num2)
# num3.shownum()


# class complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def shownum(self):
#         print(self.real,"i +",self.img,"y")
    
#     def _add_(self,num2):
#         newreal = self.real + num2.real
#         newimg = self.img +num2.img
#         return complex(newimg,newreal)
    
# num1 = complex(1,2)
# num1.shownum()

# num2 = complex(3,4)
# num2.shownum()

# num3 = num1 + num2
# num3.shownum()

# class circle:
#     def _init_(self,radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius **2
    
#     def perameter(self):
#         return 2 * self.radius * (22/7)
    
# c1 = circle(21)
# print(c1.area())
# print(c1.perameter())

# class employee:
#     def _init_ (self,role,dept,sallery):
#         self.role = role
#         self.dept = dept
#         self.sallery = sallery

#     def showdetails(self):
#         print("role =",self.role)
#         print("dept =",self.dept)
#         print("sallery =",self.sallery)

# class engineer(employee):
#     def _init_(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("engineer","IT","75000")

# eng1 = engineer("usman","18")
# eng1.showdetails()