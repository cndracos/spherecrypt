import math
from decimal import getcontext, Decimal


def round_double(val):
    getcontext().prec = 28
    return Decimal(val)


class Point:
    def __init__(self, x: Decimal, y: Decimal, z: Decimal):
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
