#is_palindrome evaluates if a string is a palindrome
#string is a str and only a str variable
# -> states that the output will be a boolean

def is_palindrome(string: str) -> bool: 
    string = string.replace(" ","").lower() #Deleting spaces and lowering case the string
    return string == string[::-1]

def run():
    print(is_palindrome(1000))

if __name__ == '__main__':
    run()

