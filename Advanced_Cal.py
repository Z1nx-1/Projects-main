
def cal1():
    while True:
        try:
            num1 = float(input("Enter first number: "))
        except ValueError:
            print("Invalid, Repeat: ")
            continue
        else:
            break
    print("(+, -, /, *)")
    while True:
        try:
            op = input("Enter operator: ")
        except ValueError:
            print("Invalid, Repeat: ")
            continue
        else:
            break
    while True:
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid, Repeat: ")
            continue
        else:
            break
    global result1
    if op == "+":
        result1 = float(num1 + num2)
        print(num1 + num2)
    elif op == "-":
        result1 = float(num1 - num2)
        print(num1 - num2)
    elif op == "/":
        result1 = float(num1 / num2)
        print(num1 / num2)
    elif op == "*":
        result1 = float(num1 * num2)
        print(num1 * num2)

    else:
        quit()


def cal2():
    cont = input("Would you like to continue? Y/N: ")
    if cont == 'Y':
        print("continuing: ")
    if cont == 'N':
        print("Quiting: ")
        quit()
    result2 = result1
    num3 = float(input("Enter first number: "))
    print("(+, -, /, *)")
    op = input("Enter operator: ")
    if op == "+":
        print(result2 + num3)
    elif op == "-":
        print(result2 - num3)
    elif op == "/":
        print(result2 / num3)
    elif op == "*":
        print(result2 * num3)
    else:
        print("Invalid operator")
        quit()


def end():
    k = input("Enter k to quit: ")
    if k == 'k':
        quit()


cal1()
cal2()
end()

print(result1)
#5340957340597843095743095743097540935903590437507435947350987034289576089723465782367895435873408r234857834753408957340895723489-7523497865324789562394786523478