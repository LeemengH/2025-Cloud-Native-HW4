# Simple calculation: square the number
try:
    print("Add two number")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum of {num1} + {num2} is {num1+num2}")
except ValueError:
    print("Invalid input. Please enter a number.")
