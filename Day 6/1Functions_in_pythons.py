#FUNCTION IN PYTHON;
                  # Functionn is a block of statements that perform a specific task.

def calc_sum (a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(1, 3)
#or

def calc_sum():
    a = int(input("enter num :"))
    b = int(input("enter num :"))

    sum = (a+b)
    print(sum)

calc_sum()



def calc_avg (a, b, c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg

calc_avg(1, 3, 4)

#or

def calc_avg():
    a = int(input("enter num :"))
    b = int(input("enter num :"))
    c = int(input("enter num :"))

    avg = (a + b + c)/3
    print(avg)

calc_avg()

#TYPES OF FUNCTION
#1) Built-in function
                   # That is already built in python
#2) User defined functions.  
