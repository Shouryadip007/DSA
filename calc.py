operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")

else:
    print("Enter a valid operator next time.")