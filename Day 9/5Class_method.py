
#CLASS METHOD:
            #A class method is bound to the class and receives the class as an implicit first argument.

#NOTE:-> static method cant access or modify class state and gennerally for utility.


class person:
    name = "usman"

    def changename(self, name):
        person.name = name

p1 = person()
p1.changename("khan")
print(p1.name)
print(person.name)
    
                    #or


class person:
    name = "usman"

    def changename(self, name):
        self.__class__.name = "khan"

p1 = person()
p1.changename("khan")
print(p1.name)
print(person.name)


                         #or


class person:
    name = "usman"

    @classmethod
    def changename(cls, name):
        cls.name = name

p1 = person()
p1.changename("khan")
print(p1.name)
print(person.name)


class student:
    def __init__(self, phy, che, bio):
        self.phy = phy
        self.che = che
        self.bio = bio
        self.percentage = str((self.phy + self.che + self.bio) / 3 ) + "%"

st1 = student(90, 80, 95)
print(st1.percentage)


class student:
    def __init__(self, phy, che, bio):
        self.phy = phy
        self.che = che
        self.bio = bio

    @property
    def percentage(self):
        return str((self.phy + self.che + self.bio) / 3 ) + "%"



st1 = student(90, 80, 95)
print(st1.percentage)

st1.phy = 96
print(st1.percentage)