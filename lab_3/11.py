class Person:
    def __init__(self, name):
        self.name = name
        
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
    def get_info(self):
        return f"{self.name} - {self.salary} - {self.department}"

manager = Manager("ahmed", 50000, "Sales")
print(manager.get_info()) # output: John - 50000 - Sales
