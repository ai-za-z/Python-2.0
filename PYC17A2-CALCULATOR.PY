def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

def divide(x,y):
    return(x/y)



print("Please enter your operation to do..\n1. Addition \n2. Subtration \n3. Divison \n4. Multiplication")
input_user = int(input("Select from the above operations...(1)(2)(3)(4)"))

first_number = int(input("Please enter your first number..."))
second_number = int(input("Please enter your second number..."))

if input_user == 1:
    print("sum =", add(first_number,second_number))
elif input_user == 2:
    print("difference =", subtract(first_number,second_number))
elif input_user == 3:
    print("product =", multiply(first_number,second_number))
elif input_user == 4:
    print("quotient =", divide(first_number,second_number))
else:
    print("Invaild input")