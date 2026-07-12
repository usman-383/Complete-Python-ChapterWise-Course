#PRACTICE PROBLEMS

#Write a function to print the length of a list.

name = [ "usman", "khan", "x5"]

def print_len(list):
    print(len(list))


print_len(name)

#Write a function to print the elements of a list in a sigle line.

name = [ "usman", "khan", "x5"]
name = ["luqman", "khan"]

print(name[0], end = " ")
print(name[1])

def print_list(list):
    for items in list:
        print(items , end=" ")

#Write a function to find the factorial of n.

n = int(input("enter num :"))
def calc_fact():
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact()


#Write a function to convert usd into pkr

def converter(usd_val):
    pkr_val = usd_val * 283
    print(usd_val, "USD =", pkr_val, "PKR")

converter(5)
