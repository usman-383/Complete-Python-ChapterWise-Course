#SUPER METHOD
          #super () method is used to access method of the parent class

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped.")
        
class Toyotacar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

car1 = Toyotacar("prius", "electric")
print(car1.type)