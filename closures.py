#this a closures beacuase: 
#a) it contains a nested function
#b) the nested function reference a greater scope value
#c) the function returns the nested fuction

def make_multiplier(x):

    def multiplier(n): #nested function
        return x * n

    return multiplier
def run():
    times10 = make_multiplier(10)
    times4 = make_multiplier(4)

    print(times10(3))
    print(times4(5))
    print(times10(times4(2)))

if __name__ == '__main__':
    run()