class Phone:
    def __init__(self,brand,price):
        self.brand = brand
        self.__price = price
my_phone = Phone("Nokia",1000)
#print(my_phone.price)
my_phone.price = 2000
print(my_phone.__price)
