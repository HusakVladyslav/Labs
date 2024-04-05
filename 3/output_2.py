from abc import ABC, abstractmethod

class ShapeCalculator(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class CircleCalculator(ShapeCalculator):
    def calculate_area(self):
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        print("Area:", area)

class RectangleCalculator(ShapeCalculator):
    def calculate_area(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print("Area:", area)

class TriangleCalculator(ShapeCalculator):
    def calculate_area(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("Area:", area)

# Приклад використання класу
calculator = CircleCalculator()
calculator.calculate_area()