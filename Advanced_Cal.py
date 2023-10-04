def cal1():
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
        else:
            break
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


def cal2(original):
    cont = input("Would you like to continue? Y/N: ")
    if cont == 'Y':
        print("continuing: ")
    if cont == 'N':
        print("Quiting: ")
        quit()
    while True:
        try:
            number2 = original
            number3 = float(input("Enter first number: "))
        except ValueError:
            print("Invalid, repeat: ")
        try:
            print("(+, -, /, *)")
            operator = input("Enter operator: ")
            if operator == "+":
                result2 = float(number2 + number3)
            elif operator == "-":
                result2 = float(number2 - number3)
            elif operator == "/":
                result2 = float(number2 / number3)
            elif operator == "*":
                result2 = float(number2 * number3)
            print(result2)
        except:
            print("Invalid operator")
        else:
            break


def end():
    k = input("Enter k to quit: ")
    if k == 'k':
        quit()


result = cal1()
cal2(result)
end()