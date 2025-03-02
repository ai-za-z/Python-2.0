class Vehicle:
    def __init__(self, capacity, fare_per_person):
        self.capacity = capacity
        self.fare_per_person = fare_per_person

    def total_fare(self):
        return self.capacity * self.fare_per_person


class Bus(Vehicle):
    def total_fare(self):
        base_fare = super().total_fare()
        maintenance_charge = base_fare * 0.10  # Additional 10% maintenance charge
        return base_fare + maintenance_charge


# Example usage:
bus = Bus(capacity=50, fare_per_person=20)
print("Total Bus Fare:", bus.total_fare())
