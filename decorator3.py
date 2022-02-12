def borders(func):
    def wrapper(text):
        #Text in a cube
        print(" " + "_" * (1 + len(text)))
        print("/" + "_" * (len(text)) + "/|")
        print("|" + " " * (len(text)) + "||")
        func("|" + text + "||")
        print("|" + "_" * (len(text)) + "|/")
    return wrapper

@borders
def cute_text(text):
    print(text)

def run():
    cute_text("Hello world")


if __name__ == '__main__':
    run()



