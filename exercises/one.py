
# todo: Crea una clase Rectangulo con métodos area() y perimetro()
class Rectangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return 2 * (self.base * self.height)


rectangle = Rectangle(12, 24)

print(f"The area of the rectangle is: {rectangle.area()}")
print(f"The perimeter of the rectangle is: {rectangle.perimeter()}")
