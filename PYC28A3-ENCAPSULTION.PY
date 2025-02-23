class Car:
    __totalcar = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        self.__speed = None
        Car.__totalcar += 1
    def gettotalcar():
        return f"This factory has produced : {Car.__totalcar}"
    def get_brand(self):
        return self.__brand
    def set_speed(self,speed):
        self.__speed = speed
    def __get_speed(self):
        return self.__speed
my_car = Car("Toyota","Supra")
my_car2 = Car("Nissan","GTR")
print(Car.gettotalcar())
print(my_car.get_brand())
print(my_car.get_speed())
my_car.set_speed(100)
print(my_car.get_speed())



