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
    global result1
    if operator == "+":
        result1 = float(number1 + number2)
    elif operator == "-":
        result1 = float(number1 - number2)
    elif operator == "/":
        result1 = float(number1 / number2)
    elif operator == "*":
        result1 = float(number1 * number2)
    print(result1)
        

def cal2():
    cont = input("Would you like to continue? Y/N: ")
    if cont == 'Y':
        print("continuing: ")
    if cont == 'N':
        print("Quiting: ")
        quit()
    result2 = result1
    number3 = float(input("Enter first number: "))
    print("(+, -, /, *)")
    operator = input("Enter operator: ")
    if operator == "+":
        result2 = (result2 + number3)
    elif operator == "-":
        result2 = (result2 - number3)
    elif operator == "/":
        result2 = (result2 / number3)
    elif operator == "*":
        result2 = (result2 * number3)
    else:
        print("Invalid operator")
        quit()
    print(result2)


def end():
    k = input("Enter k to quit: ")
    if k == 'k':
        quit()


cal1()
cal2()
end()

print(result1)