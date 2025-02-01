def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 120:
            return "Error"
        return "Even" if age % 2 == 0 else "Odd"
    except ValueError:
        return "Error"

print(check_age())