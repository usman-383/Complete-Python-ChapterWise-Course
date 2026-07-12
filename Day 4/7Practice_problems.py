# PRACTICE PROBLEMS

#1 store the following words meanings in python dictionary
     # table : "a piece of furniture" , "lists of facts and figures"
     # cat : "a small animal"

dict = {
     "cat" : "a small animal", 
     "table" : ["a piece of furniture", "lists of facts and figures"]
}
print(dict)

#2 you are given a lists of subjects for students. Assume one classroom is required for 1 sunjects. How many classroom are needed by all students

set = {"python", "c", "C++", "java", "javascript", "java", "python"}
print(set)
print(len(set))

#3 write a program to enter marks of three subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one.use sub name as key and marks as value.

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter bio : "))
marks.update({"bio" : x})

print(marks)

#4 Figure out a way to store 9 and 9.0 as separate values in the set

values = {9, "9.0"}
print(values)