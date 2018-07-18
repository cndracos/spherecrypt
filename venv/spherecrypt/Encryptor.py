import random
from ByteUtilities import ByteUtilities
from SphereCryptor import SphereCryptor
from Point import Point
from Vector import Vector


def get_encrypted_string(difficulty: int, message_bytes: bytearray, p: Point, v: Vector):
    ba = bytearray()
    ByteUtilities.coordinate_byte_array(ba, p.x, p.y, p.z)
    ByteUtilities.coordinate_byte_array(ba, v.a, v.b, v.c)
    ba.append(difficulty)
    ByteUtilities.append_message_to_byte_array(ba, message_bytes)
    return ba


class Encryptor:
    @classmethod
    def encrypt(cls, message: str, difficulty: int):
        message_bytes = bytearray(message, encoding="utf-8")

        p = Point(.7, -3, 4).normalize
        v = Vector(random.uniform(0, 1) if p.x > 0 else random.uniform(-1, 0),
                   random.uniform(0, 1) if p.y > 0 else random.uniform(-1, 0),
                   random.uniform(0, 1) if p.z > 0 else random.uniform(-1, 0))

        message_bytes = SphereCryptor.bounce_message(message_bytes, SphereCryptor.calc_next_point(p, v),
                                                     v.reflect(p), difficulty)

        return get_encrypted_string(difficulty, message_bytes, p, v)
