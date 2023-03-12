import math

class Shape:
    def __init__(self, color):
        self.color = color
        
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
        
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

rectangle = Rectangle("red", 4, 5)
print(rectangle.area())

circle = Circle("blue", 3)
print(circle.area())