#1

n = int(input("enter num :"))

for i in range (1,11):
    print(f"{n} X {i} = {n * i}")

#2

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print("hello", name)

#3

n = int(input("enter num :"))

i = 1
while i<=10:
    print(f"{n} X {i} = {n * i}")
    i+=1
#4

n = int(input("enter num :"))

for i in range (2, n):
    if (n%i == 0):
        print("number is not prime")

        break
else:
    print("number is prime")

#5

n = int(input("enter num :"))

sum = 0
i = 1

while i<=n:
    sum +=i
    i+=1
print("total sum = ",sum)


#6

n = int(input("enter num :"))
fact = 1
for i in range(1, n+1):
    fact*=i
    i+=1

print("fact = ", fact)


#7   

n = int(input("enter num :"))
for i in range (1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")

#8


n = int(input("enter num :"))
for i in range (1, n+1):
    print("*" * i, end="")
    print("")


#9
n = int(input("enter num :"))
for i in  range(1, n+1):
    if (i == 1 or i == n):
        print("*" * (n), end= "")
    else:
        print("*", end= "")
        print(" "* (n-2), end = "")
        print("*", end="")

    print("")

#10
n = int(input("enter num :"))
for i in range(1, 11):
    print(f"{n} X {11-i} = {n * (11-i)}") 