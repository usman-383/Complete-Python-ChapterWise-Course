#practice question

class circle:
    def __init__(self, radius,):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def parameter(self):
        return 2 * (22/7) * self.radius

C1 = circle(21)
print(C1.area())
print(C1.parameter())

#practice question

class employee:
    def __init__(self, role, dept, salery):
        self.role = role
        self.dept = dept
        self.salery = salery
        
    def showdetails (self):
        print("role =",self.role)
        print("dept =", self.dept)
        print("salery =", self.salery)

class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer", "IT", "75,000")
        
   

eng1 = engineer("usman", 18)
eng1.showdetails() 