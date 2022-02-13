my_set = {1, 2, 3}
print(my_set) #output : {1,2,3}

# add one element
my_set.add(4)
print(my_set) #ouput : {1,2,3,4}

# add multiple elements
my_set.update([1,2,5])
print(my_set) #ouput : {1,2,3,4,5}

# add multiple elements
my_set.update([1,6,7], (8,9), {10, 9})
print(my_set) #output : {1,2,3,4,5,5,6,7,8,9,10}

# delete element with discard
my_set.discard(10)
print(my_set) #output : {1,2,3,4,5,6,7,8,9}

# delete element with remove
my_set.remove(1)
print(my_set) #output : {2,3,4,5,6,7,8,9}

# delete an inexisting element with discard
my_set.discard(12)
print(my_set) #output : {1,2,3,4,5,6,7,8,9}
#NOTHING HAPPENS

"""# delete an inexisting element with remove
my_set.remove(12) #ERROR RAISES
print(my_set)"""

#delete a random element
my_set.pop()
print(my_set) 

#Clear set
my_set.clear()
print(my_set) #set()