my_list = [1,2,3,4,5]
my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

##### SAME AS ########
my_other_list = [1,2,3,4,5]

for element in my_other_list:
    print(element)