class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
total = 5000 + 5000 * 10 / 100
print("Total Bus fare is:", School_bus.fare())
print("The total price of everythin is", total)