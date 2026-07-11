#5String Function;
#1 ENDSWITH 

str = "usman khan"
print(str.endswith("an")) #true
print(str.endswith("kha")) #false

#2CAPITALIZE

str = "usman khan"
print(str.capitalize()) #here no change will occur in original str.
print(str)

str ="usmna khan"
str =str.capitalize() #here a change will occur in original str
print(str)

#3REPLACE 
       # to replace old value to new value
str ="usman khan"
print(str.replace("a" , "o")) #here a will replace o

str ="usman khan"
print(str.replace("usman" ,"luqman")) #here lquman will replace usman

#4FIND
    #To find a word in a string.
str ="usman khan"
print(str.find("u")) #here we find the index or location of u.

#5COUNT
 
str ="usman khan"
print(str.count("a"))