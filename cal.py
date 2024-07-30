def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("Enter your choice (1/2/3/4): ")
    if operation == '1':
        result = num1 + num2
        operation_sign = '+'
    elif operation == '2':
        result = num1 - num2
        operation_sign = '-'
    elif operation == '3':
        result = num1 * num2
        operation_sign = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_sign = '/'
        else:
            print("Error! Division by zero.")
            return
    else:
        print("Invalid input")
        return
    
    print(f"{num1} {operation_sign} {num2} = {result}")
calculator()
