#INPUT Hola,3
#OUTOUT = HolaHolaHola
def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "You can only use strings" #We assert that the input is a str type
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    repeat_3 = make_repeater_of(3)

    print(repeat_5("Fer"))
    print(repeat_3("Hello"))

if __name__ == '__main__':
    run()