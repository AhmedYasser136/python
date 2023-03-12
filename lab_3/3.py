class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def raise_salary(self, percent):
        self.salary += self.salary * percent / 100


employee = Employee("Ahmed", 30, 50000)

print("Current salary:", employee.salary)

employee.raise_salary(10)


print("New salary:", employee.salary)
