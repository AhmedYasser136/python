class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        
    def drive(self, miles):
        self.mileage += miles


car = Car("Toyota", "Camry", 2018, 20000)


print("Current mileage:", car.mileage)


car.drive(100)


print("New mileage:", car.mileage)
