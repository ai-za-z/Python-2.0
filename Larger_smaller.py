num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"The larger number is {num1}")
else:
    if num2 > num1:
        print(f"The larger number is {num2}")
    else:
        print("The numbers are equal")
