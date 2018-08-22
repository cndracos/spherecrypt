import SphereCryptor
import ByteUtilities
from Point import Point
from Vector import Vector


def decrypt(message, difficulty):
    encrypted_bytes = bytearray.fromhex(message)

    point_coordinates = ByteUtilities.byte_array_to_coordinates(encrypted_bytes, 0)
    p = Point(point_coordinates[0], point_coordinates[1], point_coordinates[2])

    vector_coordinates = ByteUtilities.byte_array_to_coordinates(encrypted_bytes, 12)
    v = Vector(vector_coordinates[0], vector_coordinates[1], vector_coordinates[2])

    message_bytes = ByteUtilities.get_message_bytes(encrypted_bytes, 24)

    SphereCryptor.calc_next_point(p, v)
    v = Vector(-v.a, -v.b, -v.c)
    message_bytes = SphereCryptor.bounce_message(message_bytes, SphereCryptor.calc_next_point(p, v),
                                                 v.reflect(p), difficulty)

    return message_bytes.decode(encoding="utf-8", errors='ignore')
