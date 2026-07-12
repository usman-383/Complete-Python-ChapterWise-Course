#FOR LOOP
       # For loop are use for sequential traversal. For traversing list, string, tuples etc

for i in range(6):  #to print nums from 0 to n-1
      print(i)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in nums :
      print(val)
else:
      print("end")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in nums :
      if(val==6):
            break
      print(val)
else:
      print("end")

#PRACTICE QUESTIONS

#Print the elements of the following list using a loop.
 # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in list:
      print(el)

#search for a number of x in this tuple by usnig loop.
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0

for el in num :
      if(el==x) :
            print("number founded at index",i)
      i += 1

#To print num from 0 to n-1

for i in range(10):
      print(i)