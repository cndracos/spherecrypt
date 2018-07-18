import math
from Point import *
from Vector import Vector
from ByteUtilities import ByteUtilities


def point_function(x, y, z):
    return (round_double(x) * round_double(y) + 1) / (round_double(z) * round_double(z) + 1)


class SphereCryptor:
    MULTIPLIER_SCALE = 2
    multiplier: bytearray

    @classmethod
    def bounce_message(cls, message: bytearray, p: Point, v: Vector, difficulty):
        cls.multiplier = ByteUtilities.to_byte_array(point_function(p.x, p.y, p.z))

        for x in range(0, len(message)):
            message[x] ^= (cls.multiplier[(x % cls.MULTIPLIER_SCALE) + 1] ^ (x + 1))

        return message if difficulty == 1 else cls.bounce_message(message, cls.calc_next_point(p, v),
                                                                  v.reflect(p), difficulty - 1)

    @classmethod
    def calc_next_point(cls, p: Point, v: Vector):
        d = round_double(v.a * v.a + v.b * v.b + v.c * v.c)
        e = round_double(2 * (v.a * p.x + v.b * p.y + v.c * p.z))
        f = round_double(p.x * p.x + p.y * p.y + p.z * p.z - 1)
        t = cls.quad_formula(d, e, f)

        p.x += t * v.a
        p.y += t * v.b
        p.z += t * v.c

        return p

    @classmethod
    def quad_formula(cls, a, b, c):
        x = (-b + Decimal(math.sqrt(b * b - 4 * a * c))) / (2 * a)
        y = (-b - Decimal(math.sqrt(b * b - 4 * a * c))) / (2 * a)
        return y if x == 0 else x
