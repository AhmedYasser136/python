class Dog(Animal, Pet):
    def __init__(self, name, owner, breed):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
        self.breed = breed
        
    def get_info(self):
        return f"{self.name} - {self.owner} - {self.breed}"

dog = Dog("Rufus", "ahmed", "Labrador")
print(dog.get_info())
