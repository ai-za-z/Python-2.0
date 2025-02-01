# taking average of Aizaz's marks in 5 subjects are 40, 50, 70, 90, 20 in english, maths, science, hindi, sst respectively

print("Enter Marks obtained in 5 subjects")

sst = int(input("enter the marks for sst: "))
eng = int(input("enter the marks for eng: "))
maths= int(input("enter the marks for maths: "))
science = int(input("enter the marks for science: "))
hindi = int(input("enter the marks for hindi: "))

# Lets calculate the percentage of marks

sum = maths+eng+science+sst+hindi

print("sum of maths, eng, science, sst and hindi")

percentage = (sum/500)*100

print(end="Percentage Mark = ")
print(percentage)