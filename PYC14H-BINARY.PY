num = int(input("Enter a number: "))

binary = ""
temp = num

while temp > 0:
    binary = str(temp % 2) + binary
    temp //= 2

print("Binary of", num, "is", binary)
