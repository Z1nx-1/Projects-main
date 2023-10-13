
def calculator():
    while True:
        try:
            number1 = float(input("Enter first number: "))
        except ValueError:
            print("Invalid, Repeat: ")
            continue
        print("(+, -, /, *)")
        try:
            operator = input("Enter operator: ")
        except ValueError:
            print("Invalid, Repeat: ")
            continue
        try:
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid, Repeat: ")
            continue
        if operator == "+":
            result = float(number1 + number2)
        elif operator == "-":
            result= float(number1 - number2)
        elif operator == "/":
            result = float(number1 / number2)
        elif operator == "*":
            result = float(number1 * number2)
        print(result)
        return result


def calculator2(original):
    while True:
        cont = input("Add another number? Y/N: ")
        if cont == 'Y':
            print("continuing: ")
        if cont == 'N':
            quit()
        print("(+, -, /, *)")
        try:
            operator = input("Enter operator: ")
        except ValueError:
            print("Invalid, Repeat: ")
            continue
        try:
            number3 = float(input("Enter first number: "))
        except ValueError:
            print("Invalid, Repeat: ")
            continue
        if operator == "+":
            result2 = float(original + number3)
        elif operator == "-":
            result2 = float(original - number3)
        elif operator == "/":
            result2 = float(original / number3)
        elif operator == "*":
            result2 = float(original * number3)
        print(result2)
        loop = input('1: add another number:\n2: start over: ')
        if loop == str('1'):
            pass
        if loop == str('2'):
            calculator()
        return result2

            
def calculator_loop(result2):
    number = input(float('Enter number: '))
    print("(+, -, /, *)")
    operator = input('Enter operator:')
    if operator == "+":
        result = float(result + number)
    elif operator == "-":
        result = float(result - number)
    elif operator == "/":
        result = float(result / number)
    elif operator == "*":
        result = float(result * number)
    print(result)

    


original = calculator()
result2 = calculator2(original)
calculator_loop(result2)
