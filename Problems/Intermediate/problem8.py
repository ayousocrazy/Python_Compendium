"""
Function Overriding + Class Behavior Test
Create:
-A base class Shape
-Child classes Circle, Rectangle

Each must have:
    area() method
    perimeter() method

Requirement:
-Override methods properly.
-Write a function that accepts a list of shape objects and prints their details.
"""
import math

class Shape:
    def area(self):
        raise NotImplementedError
    
    def perimeter(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


def show_details(shapes):
    for s in shapes:
        print(f"Shape: {s.__class__.__name__}")
        print(f"Area: {s.area()}")
        print(f"Perimeter: {s.perimeter()}")


# TESTS
c1 = Circle(6)
r1 = Rectangle(33, 22)

shapes = [c1, r1]
show_details(shapes)