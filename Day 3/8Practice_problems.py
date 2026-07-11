#PRACTICE PROBLEM


#1 wirte a program in which user enter 3 fvt movies and print thier list.

move = []
move.append(input("enter first movie : "))
move.append(input("enter second movie : "))
move.append(input("enter third movie : "))
print(move)

#2 write a program to check if a list contain a palindrome of elements.

list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")

else:
    ("not palindrome")


#3 write a program to count the number of student with the "A" grade in the following tuple.
#["C", "D", "A", "A", "B", "B", "A"]

grade = ["C", "D", "A", "A", "B", "B", "A"]
print(grade.count("A"))

#4 sort that list from "A" TO "B"

grade = ["C", "D", "A", "A", "B", "B", "A"]
print(grade.sort())
print(grade)