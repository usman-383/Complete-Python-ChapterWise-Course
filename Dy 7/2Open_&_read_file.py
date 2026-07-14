#How to open and  read a file

f= open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close


f= open("demo.txt", "r")
line1 = f.readline()
print(line1)
print(type(data))
f.close
