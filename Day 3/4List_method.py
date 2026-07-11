#LIST METHOD

#1APPEND
     # To add a number or words at the end of list or string.

list = [1, 2, 3]
list.append(4)  #4 will be add at the end of list
print(list)

#2SORTING
      #To arrange thing in correct list. means asceding or descending

#ascending order

list = [2, 1, 3]
print(list.sort())
print(list)

#Descending order

list = [1, 2, 3, 4]
print(list.sort(reverse=True))
print(list)

#3REVERSE LIST

list = [5, 4, 9]
print(list.reverse())
print(list)

#4INSERTING
         #To add one element before another.

list = [1, 2, 4, 5]
print(list.insert(2, 3))
print(list)

#5REMOVE INDEX
 
list = [2, 1, 3, 1]
print(list.remove(1))
print(list)