import math


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def scale(self, scale):
        return Point(self.x * scale, self.y * scale, self.z * scale)

    @property
    def normalize(self):
        magnitude = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        self.x /= magnitude
        self.y /= magnitude
        self.z /= magnitude
        return self
