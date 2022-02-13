my_set1 = {1,2,3}
my_set2 = {3,4,5}

#union
my_set3 = my_set1 | my_set2
print(my_set3)

#intersection
my_set4 = my_set1 & my_set2
print(my_set4)

#Difference
my_set5 = my_set1 - my_set2
my_set6 = my_set2 - my_set1
print(my_set5)
print(my_set6)

#Symmetric difference
my_set7 = my_set1 ^ my_set2
print(my_set7)