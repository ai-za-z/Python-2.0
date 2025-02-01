print("Welcome to grading system.....")

sub1 = float(input("Enter your subject 1 marks obtained..."))
sub2 = float(input("Enter your subject 2 marks obtained..."))
sub3 = float(input("Enter your subject 3 marks obtained..."))
sub4 = float(input("Enter your subject 4 marks obtained..."))
sub5 = float(input("Enter your subject 5 marks obtained..."))
sub6 = float(input("Enter your subject 6 marks obtained..."))


average_marks = (sub1+sub2+sub3+sub4+sub5+sub6) / 5 

if average_marks>=90 and average_marks<=100:
    print(f"Walah!! you got grade A. {average_marks}")
elif average_marks>=80 and average_marks<=90:
    print(f"Nice!!! you got grade B. {average_marks}")
elif average_marks>=70 and average_marks<=80:
    print(f"Nice!!! you got grade C. {average_marks}")
elif average_marks>=60 and average_marks<=70:
    print(f"Nice!!! you got grade E. {average_marks}")
elif average_marks>=50 and average_marks<=60:
    print(f"Nice!!! you got grade D. {average_marks}")
elif average_marks>=40 and average_marks<=50:
    print(f"Nice!!! you got grade F. {average_marks}")
else:
    print(f"You failed in your exams {average_marks}")