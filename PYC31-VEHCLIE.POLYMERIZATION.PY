class BMW:
    def brand(self):
        return "This is a BMW."
    
    def speed(self):
        return "BMW has a top speed of 250 km/h."
    
    def fuel_type(self):
        return "BMW runs on petrol or diesel."

class Ferrari:
    def brand(self):
        return "This is a Ferrari."
    
    def speed(self):
        return "Ferrari has a top speed of 340 km/h."
    
    def fuel_type(self):
        return "Ferrari runs on high-performance petrol."

# Function demonstrating polymorphism
def vehicle_info(vehicle):
    print(vehicle.brand())
    print(vehicle.speed())
    print(vehicle.fuel_type())

# Creating objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Calling the function with different objects
print("BMW Details:")
vehicle_info(bmw_car)
print("\nFerrari Details:")
vehicle_info(ferrari_car)
