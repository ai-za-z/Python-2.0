weight = float(input("Enter your weight in KGs: "))
height = float(input("ENter your height in Meters: "))


bmi = round(weight / (height**2), 2)

if bmi < 18.5:
    print(f"BMI: {bmi}.\nYou are underweighted...")
elif bmi >= 18.5 and bmi <+ 24.9:
    print(f"BMI: {bmi}.\nYou BMI is normal...")
elif bmi >= 25 and bmi <+ 29.9:
    print(f"BMI: {bmi}.\nYou are over weighted....")
else:
    print(f"BMI: {bmi}.\nYou are obese")