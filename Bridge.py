# Abstraction
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

# Concrete Abstraction
class Circle(Shape):
    def draw(self):
        self.color.paint("Circle")

class Square(Shape):
    def draw(self):
        self.color.paint("Square")

# Implementation
class Color:
    def paint(self, shape):
        pass

# Concrete Implementations
class Red(Color):
    def paint(self, shape):
        print(f"Drawing a red {shape}")

class Blue(Color):
    def paint(self, shape):
        print(f"Drawing a blue {shape}")

# Client code
def main():
    red_color = Red()
    blue_color = Blue()

    red_circle = Circle(red_color)
    blue_circle = Circle(blue_color)

    red_square = Square(red_color)
    blue_square = Square(blue_color)

    shapes = [red_circle, blue_circle, red_square, blue_square]

    for shape in shapes:
        shape.draw()

if __name__ == "__main__":
    main()
