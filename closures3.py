from __future__ import division


def make_division_by(n):
    """This closure returns a function that 
    returns the division of an x number by n"""
    def division_by(x: float)-> float: 
        assert n != 0, "You cannot divide by 0"
        return x / n
    return division_by


def run():
    division_by_3 = make_division_by(3)
    division_by_5 = make_division_by(5)
    division_by_18 = make_division_by(18)

    print(division_by_3(18))
    print(division_by_5(100))
    print(division_by_18(54))

if __name__ == '__main__':
    run()