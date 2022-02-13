def gen():
    """Generator example"""

    print('Hello world')
    n = 0
    yield n 

    print('Hello heaven')
    n = 1
    yield n

    print('Hello hell')
    n = 2
    yield n 

a = gen()
for n in range(0,3):
    next(a)