# Program to check if a number is positive, negative, or zero

# Input from the user
number = float(input("Enter a number: "))

# Conditional checks
if number > 0:
    print("The number is positive.")
else:
    if number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
