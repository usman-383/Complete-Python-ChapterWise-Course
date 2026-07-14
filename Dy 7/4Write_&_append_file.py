#How to writing and appending a file 

f = open("demo.txt", "w")
f.write("my name is khan")  #the old file will be replace by this sentence.
f.close()


f = ("demo.txt", "a")
f.write("\nmy name is khan")  #here in this case this sentence will be add in the old file with next line
f.close()

f = open("demo.txt", "r+")
f.write("abc")    #here in this  case the first three alphabits will be replace by this alphabits.
print(f.read())     
f.close()

f = open("demo.txt", "w+")
print(f.read())  #here the whole file will be remove because in wrrting mode the whole file reomved 
f.write("hey")
f.close()


f = open("demo.txt", "a+")
print(f.read())  
f.write("hey")  #here in this case hey will be add at the end of file
f.close()
