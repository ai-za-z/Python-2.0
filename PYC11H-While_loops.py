number = input("Enter a number: ")
count = 0
i = 0

while i < len(number):
    if number[i] != "-":
        count += 1
    i += 1

print("The total number of digits is:", count, 100, "")
