class Vehicle:
    def max_speed(self):
        return "Max speed is 80 km/h"

class Car(Vehicle):
    def max_speed(self):
        return "Max speed is 150 km/h"


v = Vehicle()
c = Car()

print(v.max_speed())
print(c.max_speed())  # Overridden method
