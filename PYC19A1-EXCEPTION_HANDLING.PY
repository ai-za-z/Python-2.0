try:
    num = int(input("Enter the number..."))
    print(f"The number you entered is", (num))
except ValueError as ab:
    print("Exception", ab)
