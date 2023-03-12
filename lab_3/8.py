class Vehicle:
    def __init__(self, speed):
        self.speed = speed
        
class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand
        
    def get_info(self):
        return f"{self.brand} - {self.speed} km/h"

car = Car(120, "Toyota")
print(car.get_info()) 