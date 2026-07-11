#TYPE OF OPERATORS
                 #An operator is a symble thst perform a certain operation between operands.
#1ARITMETIC OPERATOR
                  # Arithmetic operator means sum, difference,multiplication, divisoin,power and reminder.
a= 10
b= 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #% means modelo which means reminder of the two value
print(a ** b) #power

#2RENATIONAL OPERATOR
                   #Renational operator means equal or not equal,less or greater than, less or equal, greater or equal.
a = 10
b = 3
print(a==b) #fals
print(a!=b) #true
print(a>=b) #true
print(a<=b) #fals
print(a> b) #true
print(a< b) #fals

#3ASSIGNMENTAL OPERATORS
                    
num = 10
num = num +10 #means 10+10 = 20
       #or
num += 10
print(num)
print("num :",num)

num = 10
num =10 -10 #means 10-10=0
print(num)
  #or
num-=10 #means 10-10=0
print("num :" , num)

num = 10
num *=5 #*means multiply
print("num :", num)

num = 10
num /=5 #/ means division
print("num :" , num)

num =10
num %=5 #%means reminder
print("num :", num)

num =10
num **= 5 #** means power
print("num :", num)

#4LOGICAL OPERATORS
#Not operator
print(not False) #true
print(not True) #Fals

a = 50
b = 30
print(not False)
print(not(a>b))

#AND OPERATOS
val1 =True
val2= True
print("and operator :" , val1 and val2)

#OR OPERATOR

val1 =True
val2 =False
print("OR operator:", val1 or val2)
