from ByteUtilities import ByteUtilities
from Point import Point
from Vector import Vector
from SphereCryptor import *


class Decryptor:

    @classmethod
    def decrypt(cls, message: bytearray):
        #message_bytes = bytearray(message, encoding ="utf-8")

        point_coordinates = ByteUtilities.byte_array_to_coordinates(message, 0)
        p = Point(point_coordinates[0], point_coordinates[1], point_coordinates[2])

        vector_coordinates = ByteUtilities.byte_array_to_coordinates(message, 21)
        v = Vector(vector_coordinates[0], vector_coordinates[1], vector_coordinates[2])

        difficulty: int = message[42]

        message_bytes = ByteUtilities.get_message_bytes(message, 43)

        SphereCryptor.calc_next_point(p, v)
        v = Vector(-v.a, -v.b, -v.c)
        message_bytes = SphereCryptor.bounce_message(message_bytes, SphereCryptor.calc_next_point(p, v), v.reflect(p), difficulty)

        return message_bytes
