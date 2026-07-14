#PRACTICE QUESTIONS

#1)create a new file "practice.txt" using pythod and add the following data on it

# Hi everyone
# We are learning file i/o
# Using java
# I like programming in java


with open ("practice.txt", "w") as f:
    f.write("hi everyone.\nwe are learning file i/o\n")
    f.write("using java.\ni like programming in java")


#Write a function that replace all occurance of "java" with "python" in the above file.

with open ("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java","python")
print(new_data)

with open ("practice.txt", "w") as f:
    f.write(new_data)

#search if the word learning exist in the file or not  
word = "learning"
with open ("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

def check_for_world():
    word = "learning"
    with open ("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")

check_for_world()

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no +=1
    return -1        

#From a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split (",")
    for val in nums:
        if (int(val) % 2 == 0):
            count +=1

print(count)




