# SET METHODS

# 1 .ADD METHOD

collection = set()

collection.add(1)
collection.add(2)
collection.add('usman') #string
collection.add((1, 2, 3))  #tuple

#collection.add([1, 2, 3])  #list

print(collection)

#2 REMOVE

collection = {1, 2, 3, 4, 5}

collection.remove(5)
collection.remove(4)
print(collection)

#3 CLEAR METHOD

collection = {1, 2, 3}
collection.clear()
print(collection)

#4 POP VALUE

collection = {1, 2, 3}
collection.pop()   #remove one value randomly.
print(collection)


#5 UNION

set1 = {1, 2, 3}
set2 = {3, 4, 5}
 
print(set1.union(set2))  #{1, 2, 3, 4, 5}


#6 INTERSECTION

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2))  #{2, 3}
