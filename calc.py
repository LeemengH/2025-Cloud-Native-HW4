# Simple calculation: square the number
try:
    num = float(input("Enter a number: "))
    print(f"The square of {num} is {num ** 2}")
except ValueError:
    print("Invalid input. Please enter a number.")
