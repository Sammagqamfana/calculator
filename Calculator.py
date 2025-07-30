num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Validate input
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Please enter valid numbers.")
    exit()

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The quotient of {num1} and {num2} is: {result}")
else:
    print("Invalid operation.")