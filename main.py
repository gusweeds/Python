# Simple arithmetic calculator program 

operator = input("Enter the operator (+, -, *, /): ")
 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
    print(round(result, 3))

elif operator == '-':
    result = num1 - num2
    print(round(result, 3))

elif operator == '*':
    result = num1 * num2
    print(round(result, 3))

elif operator == '/':
    if num2 == 0:
        print("Error! Division by zero.")
    
    else: 
        result = num1 / num2
        print(round(result, 3))
    
else:
    print(f"{operator} is not a valid operator.")


