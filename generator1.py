import time

def fibu_gen():
    a = 0
    b = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield a
        elif counter == 1:
            counter += 1
            yield b
        else:
            aux = a + b
            a, b = b, aux
            counter += 1
            yield aux

def run ():
    fibu = fibu_gen() #Instancing generator
    for element in range(0,11):
        print(next(fibu))
        time.sleep(0.5) #Waits 0.5 second


if __name__ == '__main__':
    run()