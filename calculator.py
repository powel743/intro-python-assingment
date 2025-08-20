#ask user for two numbers
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
#Ask user for the operation
operation = input("Enter operation (+,-,*,/): ")
#Performing the operation
if operation == '+':
    result = nim1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0: #avoid division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Divsion by zero not allowed.")
else:
    print("Error: operation invalid. please use +, -, *, or /")