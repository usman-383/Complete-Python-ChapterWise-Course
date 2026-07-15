
raise #is use for crashing a program by raising an error
a = int(input("Enter number: "))
b = int(input("Enter number: "))
if(a == 0):
    raise ZeroDivisionError("Hey our program is not ment to a number divide by zero")
else:
    print(f"The division a/b is {a/b}")



#Else
try:
    a = int(input("Enter number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("Hey i am inside else")