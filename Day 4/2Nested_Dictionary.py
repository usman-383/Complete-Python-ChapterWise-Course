#NESTED DICTIONARIES

student = {
     "name": "usman",
     "subjects" : {
          "phy" : 95,
          "che": 99,
          "bio" : 98
     }
}

print(student)
print(student["subjects"])
print(student["subjects"] ["che"])