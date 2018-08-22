import math
import ByteUtilities
from Point import *
from Vector import Vector

MULTIPLIER_SCALE = 2


def bounce_message(message, p, v, difficulty):
    multiplier = ByteUtilities.to_byte_array((p.x * p.y + 1) / (p.z * p.z + 1))

    for x in range(0, len(message)):
        message[x] ^= (multiplier[(x % MULTIPLIER_SCALE) + 1] ^ (x + 1))

    return message if difficulty == 1 else bounce_message(message, calc_next_point(p, v),
                                                          v.reflect(p), difficulty - 1)


def calc_next_point(p, v):
    d = v.a * v.a + v.b * v.b + v.c * v.c
    e = 2 * (v.a * p.x + v.b * p.y + v.c * p.z)
    f = p.x * p.x + p.y * p.y + p.z * p.z - 1
    t = quad_formula(d, e, f)

    p.x += float(t) * v.a
    p.y += float(t) * v.b
    p.z += float(t) * v.c

    return p


def quad_formula(a, b, c):
    x = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    y = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return y if x == 0 else x
