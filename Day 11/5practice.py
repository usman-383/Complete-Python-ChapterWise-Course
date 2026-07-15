#2
name = str(input("Enter name: "))
marks = int(input("Enter marks: "))
phone_number = int(input("Enter phone number: "))

s = "The name of the student is {}, his marks is {},his phone number is {}".format(name,marks,phone_number)
print(s)

#3

table = [str(7*i) for i in range(1,11)]

s = "\n".join(table)
print(s)

#4
from contextlib import redirect_stderr
from functools import divisible5, reduce
from operator import truediv
def devisible5(n):
    if (n%5 == 0):
        return True
    return False
a = [1, 5, 2, 4, 5, 56 ,5667,878 ,89, ]
f = list(filter(divisible5,a))

print(f)

#5
l = [1, 5, 2, 4, 5, 56 ,5667,878 ,89, ]
def greater(a,b):
    if (a>b):
        return a
    return b
print(reduce(greater,l))

#6

