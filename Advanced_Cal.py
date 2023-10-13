while True:    
    def calculator():
        while True:
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


    def calculator2(first_result):
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
                    number3 = float(input("Enter third number: "))
                except ValueError:
                    print("Invalid, Repeat: ")
                    continue
                if operator == "+":
                    second_result = float(first_result + number3)
                elif operator == "-":
                    second_result = float(first_result - number3)
                elif operator == "/":
                    second_result = float(first_result / number3)
                elif operator == "*":
                    second_result = float(first_result * number3)
                print(second_result)
                return second_result
        

    original_result = calculator()
    second_result = calculator2(original_result)