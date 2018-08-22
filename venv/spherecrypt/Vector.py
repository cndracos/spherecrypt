from Point import Point


class Vector:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def reflect(self, point):
        scaled_point = point.scale(2 * self.dot(point))
        self.mutate(scaled_point.x, scaled_point.y, scaled_point.z, lambda x, y: x - y)
        return self

    def dot(self, other):
        return self.a * other.x + self.b * other.y + self.c * other.z

    def mutate(self, x, y, z, func):
        self.a = func(self.a, x)
        self.b = func(self.b, y)
        self.c = func(self.c, z)
