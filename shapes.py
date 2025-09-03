class Rectangle:

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def describe(self) -> str:
        return f"A rectangle with width {self.width} cm and height {self.height} cm."


class Circle:

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def describe(self) -> str:
        return f"A circle with radius {self.radius} cm."


class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def describe(self) -> str:
        return f"A triangle with base {self.base} cm and height {self.height} cm."
