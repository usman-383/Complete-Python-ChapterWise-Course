#DICTIONARY METHODS
student = {
     "name": "usman",
     "subjects" : {
          "phy" : 95,
          "che": 99,
          "bio" : 98
     }
}

#1.keys    
       # return all keys

print(student.keys())
print(list(student.keys()))
print(len(student))

print(len(list(student.keys())))

#2.values
       # returns all values

print(student.values())
print(list(student.values()))
print(len(student))

#3 .items:
        # return all (key, val) pairs as tuples.

print(student.items())
print(list(student.items()))
print(len(student))

#4.get :
      # return the key according to vale.

print(student["name"])
print(student.get("name"))


#5 update :
          # inserts the specified items to the dictionary.

student = {
     "name": "usman",
     "subjects" : {
          "phy" : 95,
          "che": 99,
          "bio" : 98
     }
}

student.update({"city": "peshawar"})
print(student)
