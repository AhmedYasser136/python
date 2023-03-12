class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rect = Rectangle(3, 4)

area = rect.area()

print("The area of the rectangle is:", area)
