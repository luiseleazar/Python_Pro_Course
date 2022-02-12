from datetime import datetime
from typing import final

def execution_time(func):
    def wrap(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(str(time_elapsed.total_seconds()) + " seconds has passed")
    return wrap

@execution_time
def random_func():
    for _ in range(1,1000000):
        pass

@execution_time
def suma(a: int, b: int)-> int:
    return a + b

@execution_time
def salute(name="name"):
    print("Hi, "+ name)


def run():
    random_func()
    suma(7,3)
    salute("Luis")


if __name__ == '__main__':
    run()