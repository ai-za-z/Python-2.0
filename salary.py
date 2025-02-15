salary = float(input("Enter your salary: "))
experience = int(input("Enter your years of experience: "))
if experience > 5:
    salary += salary * 0.10  # Adding 10% bonus
    print(f"New salary with bonus: {salary:.2f}")
else:
    print(f"Salary: {salary:.2f}")
