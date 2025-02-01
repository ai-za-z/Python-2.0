a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

a, b, c, d = b, c, a, d

print("After swapping:")
print("First number:", a)
print("Second number:", b)
print("Third number:", c)
print("Fourth number:", d)
