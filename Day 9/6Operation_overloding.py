#POLYMORPHISM:OPERATOR OVERLOADING
#When the same operator is allowed to have different meaning according to the contex.


class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def shownumber(self):
        print(self.real, "i +", self.imag, "j")

    def add(self, num2):
        newreal = self.real + num2.real
        newimag = self.imag + num2.imag
        return complex(newreal, newimag)

num1 = complex(1, 5)
num1.shownumber()

num2 = complex(2, 4)
num2.shownumber()

num3 = num1.add(num2)
num3.shownumber()
 
                       #or

class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def shownumber(self):
        print(self.real, "i +", self.imag, "j")

    def __add__(self, num2):
        newreal = self.real + num2.real
        newimag = self.imag + num2.imag
        return complex(newreal, newimag)

num1 = complex(1, 5)
num1.shownumber()

num2 = complex(2, 4)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()