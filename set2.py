def delete_repeated(my_list):
    #my_list = set(my_list)
    #my_list = list(my_list)
    #return my_list
    return list(set(my_list))


def run():
    my_list = [1,1,1,2,3,3,2,4,3,2]
    print(delete_repeated(my_list))

if __name__ == '__main__':
    run()