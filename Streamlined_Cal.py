number1 = float(input('Enter your first number: '))
while True:
    operator = input('Enter operator\n(+, -, /, *): ')
    number2 = float(input('Enter your second number: '))
    if operator == '+':
        number1 += number2
    elif operator == '-':
        number1 -= number2
    elif operator == '/':
        number1 /= number2
    elif operator == '*':
        number1 *= number2
    result = number1
    print(result)