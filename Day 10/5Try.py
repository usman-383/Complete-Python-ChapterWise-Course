
#If you want to manage error in your code, you can just use try except to show no error in your code.
try:
    a = int(input("Enter number: "))
    print(a)

except Exception as e:
    print(e)

print("Thanks")