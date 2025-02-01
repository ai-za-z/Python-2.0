medical_clearence = str(input("Do you have any medical issue 'y' or 'n'..."))
attendence = int(input("What is your attendence rate..."))

if medical_clearence == 'y':
        print("You are allowed..")
else:
    if attendence>100:
        print("You are allowed to enter in your exams...")
    else:
        print("You are not allowed to enter in your exams...")
    

