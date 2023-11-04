number1 = float(input('Enter your first number: '))
operator = input('Enter operator\n(+, -, /, *): ')
number2 = float(input('Enter your second number: '))
if operator == '+':
    result = float(number1 + number2)
elif operator == '-':
    result = float(number1 - number2)
elif operator == '/':
    result = float(number1 / number2)
elif operator == '*':
    result = float(number1 * number2)
print(result)
while True:
    next_number = float(input('Enter your next number: '))
    operator2 = input('Enter operator\n(+, -, /, *): ')
    if operator2 == '+':
        result2 = float(result + next_number)
    elif operator2 == '-':
        result2 = float(result - next_number)
    elif operator2 == '/':
        result2 = float(result / next_number)
    elif operator2 == '*':
        result2 = float(result * next_number)
    print('\n', result2, '\n')
    result = result2
    
    
    