charter = input("Enter a character: ")

if len(charter) == 1:
    if (charter >= 'A' and charter <= 'Z') or (charter >= 'a' and charter <= 'z'):
        print(f"{charter} is an alphabet.")
    else:
        print(f"{charter} is not an alphabet.")
else:
    print("Please enter only one character.")
