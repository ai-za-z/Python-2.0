new_list = [1,2,3,4,5,6,7,8,9]

even = [x for x in new_list if x%2==0]
print(even)



mydict = {str(x):x**2 for x in [1,2,3,4,5,6,7,8,9]}
print(mydict)

def square(x):
    return x*x


numbers = (1,2,3,4,5,6,7,8,9)
result = map(square, numbers)
print(list(result))

name = ["Aizaz","Thahira","Mansha","Sabit"]
roll_no = [1,2,3,4]

name_and_rollno = zip(name,roll_no)

print(list(name_and_rollno))





ages = [19,17,34,89]
for i in ages:
    if i<=18:
        print("Age not allowed",ages )
        print(exit)
        exit()
    else:
        print("Allowed")