def upper_case(func):
    def wrap(text):
        return func(text).upper()
    return wrap


@upper_case
def message(name):
    return f'{name}, you recieved a message'
def run():
    print(message('Luis'))


if __name__ == '__main__':
    run()
    