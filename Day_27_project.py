import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius
    def calculate_circle_area(self):
        return math.pi * self.radius**2

radius = int(input("Input the radius of the circle: "))

circle = Circle(radius)

perimeter = circle.calculate_circle_perimeter()
area = circle.calculate_circle_area()

print("Perimeter of the circle:", perimeter)
print("Area of the circle:", area)