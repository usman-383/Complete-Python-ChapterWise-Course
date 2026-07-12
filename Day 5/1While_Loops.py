#LOOPS:
      # Loops are use to repeat instructions.

#TYPES OF LOOP

#1) While loop

i = 1

while  i <= 5 :     # to print hey 5 times 
    print("hey")
    i += 1

i = 1

while i <= 1000 :  # to print numbers from 1 to 1000 from lower to higher
      print(i)
      i += 1

i = 5

while i >= 1:
      print(i)  # to print from 5 to 1 means from greaater to smaller
      i -= 1


# PRACTICE   QUESTIONS
#1) PRINT NUMBER FROM 1 TO 100

num = 1
while num<= 100:
      print(num)
      
      num += 1





#2)Print numbers from 100 to 1

num = 100
while num>= 1:
      print(num)
      
      num -= 1


#3) print the multiplication table of n

n = int(input("ennter num :"))

i = 1
while i<= 10:
      print(n*i)

      i+=1

#4) Print the list [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

i = 0

while i <len(num):
      print(num[i])

      i += 1

#5) search for a number x in this tuple using loop

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

x = 36
i = 0

while i < len(nums):
      if(num[i] == x):
            print("found at idx", i)

      i += 1