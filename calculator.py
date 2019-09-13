import math


def add(a, b):
    # additions calculation
    return a+b


def substr(a, b):
    # substractions calculation
    return a-b


def mult(a, b):
    # multiptications calculation
    return a*b


def div(a, b):
    # divisions calculation
    return a/b


def power(a, b):
    # powering calculation
    return a**b


def readfloat():
    # receiving and checking from user a number for a calculation
    converted = False
    user_numbers = 0
    while not converted:
        try:
            user_numbers = float(input("Type a number:\n"))
            converted = True
        except ValueError:
            print("It's not a number")
    return user_numbers


def readsign():
    # receiving from user a sign of operation for a calculation
    user_signs = ''
    while not iscorrectsign(user_signs): # TODO ASK THE QUESTION ABOUT HARDCODING FUNCTION IN FUNCTION(AS ARGUMENT?)!!!
        user_signs = input("Type the formulas symbol:\n")
    return user_signs


def iscorrectsign(sign):
    # checking operations sign received from user
    if sign == "+":
        return True
    if sign == "-":
        return True
    if sign == "*":
        return True
    if sign == "/":
        return True
    if sign == "**":
        return True
    return False


def calculate(a, b, sign):
    # receiving user numbers and sign, calculate and return a result
    if sign == "+":
        return add(a, b)
    if sign == "-":
        return substr(a, b)
    if sign == "*":
        return mult(a, b)
    if sign == "/":
        return div(a, b)
    if sign == "**":
        return power(a, b)


def display(a, b, c, sign):
    # displaying a calculations result
    print(f"Your result is:\n{a} {sign} {b} = {c}")

#code snippet
def main():
    print("There is my calculator")
    question = ""
    while question != 'no':
        num1 = readfloat()
        sign = readsign()
        num2 = readfloat()
        if sign == "/": 
            while num2 == 0:
                print("Division by zero is forbidden, type a correct number")
                num2 = readfloat()    
        result = calculate(num1, num2, sign)
        display(num1, num2, result, sign)
        question = input("Want to continue? yes/no\n")
if __name__ == "__main__":
    main()