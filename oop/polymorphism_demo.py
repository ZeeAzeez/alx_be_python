import math

class Shape:
    def area(self):
        """Calculate the area of the shape. Must be overridden in derived classes."""
        raise NotImplementedError("Derived classes must override this method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2
