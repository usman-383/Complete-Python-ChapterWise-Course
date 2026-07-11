#PRACTICE QUESTIONS

#1 write a program to check if a number entered by the user is odd or even

num = int(input("enter number :"))

rem = num % 2

if(rem == 0):
      print("enen")
else:
      print("odd")

#2 write a program to find the greatest of 3 numbers entered by the user.

a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))

if(a > b and a > c):
      print("first number is largest" , a)
elif(b > c):
      print("second number is largest" , b )

else:
      print("third is largest number " , c)

#3 write a program to check if a number is a multiple of 7 or not.

num = int(input("enter number :"))

if(num % 7== 0):
      print("yes")
else:
    print("no")

