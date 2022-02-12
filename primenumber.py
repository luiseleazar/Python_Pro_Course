#is_prime evaluates if a given number is prime or not
#number: int indicates that the input must be an integer
#->bool indicates that the output will be a boolean

def is_prime(number: int) -> bool:
    flag = False
    if number > 1:
        for i in range(2, number):
            if number%i==0: 
                flag = False
                break
            else:
                flag = True
    return flag
          
    

def run():
    print(is_prime("a"))

if __name__ == '__main__':
    run()