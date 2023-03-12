class Shape:
    def __init__(self, color):
        self.color = color
        
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
