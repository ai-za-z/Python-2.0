class Car:
    def stop(self):
        print("The car is stopping")
    def start(self):
        print("The car is starting")
#my_car = Car()
#my_car.start()
#my_car.stop()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
aizaz = Person("aizaz",16)
#print(aizaz.name)
#print(aizaz.age)


class Example:
    def __init__(self):
        print("Object is created")
    def __del__(self):
        print("Object is destroyed")
obj = Example()
del obj



fruits = ["Apple","Banana","Cherry"]
for index, fruit in enumerate(fruits):
    print(index,fruit)