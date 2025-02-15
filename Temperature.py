fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
if celsius < 0:
    print("It's freezing!")
else:
    print(f"Temperature in Celsius: {celsius:.2f}")
