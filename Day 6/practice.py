list = ["usman", "x5"]

def print_len(list):
    print(len(list))

print_len(list)


#2
name = ["usman", "khan"]
print(name[0], end = " ")
print(name[1])

def print_list(list):
    for items in list:
        print(items, end = " ")

#3

n = int(input("enter num :"))
def fact():
    fact = 1
    for i in range(1, n+1):
        fact *=i
    print(fact)

fact()

#4
usd_val = int(input("enter usd :"))
def converter():
    pkr_val = usd_val * 283
    print(usd_val, "USD=", pkr_val, "PKR")
converter()


#5

def factorial(n):
    if (n == 1  or n == 0):
        return 1
    return n * factorial(n-1)
n = int(input("enter num :"))
print(f"factorial of this number is :{factorial(n)}")


#6

def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)

show(5)

#7

def sum(n):
    if  (n == 0):
        return 0
    return n + sum(n-1)
n = int(input("enter num :"))
print("sum of this number is :",sum(n-1) +n)



#
def greatest():
    a = int(input("enter number :"))
    b = int(input("enter number :"))
    c = int(input("enter number :"))

    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
print(greatest())

#
def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter number: "))
print(f_to_c(f))

#or

def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter number: "))
c = f_to_c(f)
print(f"{round(c,2)} degree c")

#
def pattern(n):
    if (n == 0):
        return
    print("*" * n)
    pattern(n-1)

pattern(5)

#
def inch_to_cm(n):
    return n * 2.54
n = int(input("Enter inches :"))
print("this number of inches in cm is: ", n*2.54)