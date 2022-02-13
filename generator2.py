import time

def fibu_gen(max):
    a = 0
    b = 1
    counter = 0
    while max > counter:
        yield a
        a, b = b, a+b
        counter += 1
    

def run ():
    fibu = fibu_gen(10) #Instancing generator
    for element in fibu:
        print(element)
        time.sleep(0.5) #Waits 0.5 second


if __name__ == '__main__':
    run()