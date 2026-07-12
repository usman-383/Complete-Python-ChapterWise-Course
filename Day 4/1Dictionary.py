#DICTIONARY IN PYTHON:
                     #Dictionary are used to store data values in key:value pairs. They are unorder, mutable(changeable) and dont allow duplicate keys.

info = {
     "name" : "usman",
     "subjects" : ["python", "c", "jawa"], #list
     "topics" :("dict", "set"),           #tuples
     "age" : 18, 
     "marks" : 995.5 

}
print(info)
print(type(info))
print(info["name"])
print(info["subjects"])
print(info["age"])

info["name"] = "usman"  #replace the name usman ot another name
info["nic name"] ="x5"
print(info)

null_dict = {}
print(null_dict)
null_dict["name " ] = "usman"
print(null_dict)