class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print(f"{self.name} has been destroyed")

person1 = Person("ahmed", 25)
