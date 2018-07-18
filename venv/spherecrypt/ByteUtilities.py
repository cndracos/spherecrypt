import struct


class ByteUtilities:

    @classmethod
    def get_message_bytes(cls, ba: bytearray, offset):
        message = bytearray()
        for x in range(offset, len(ba)):
            message.append(ba[x])
        return message

    @classmethod
    def to_byte_array(cls, value):
        return bytearray(struct.pack(">L", value))

    @classmethod
    def coordinate_byte_array(cls, ba: bytearray, x, y, z):
        cls.byte_array_append(ba, cls.to_byte_array(x))
        cls.byte_array_append(ba, cls.to_byte_array(y))
        cls.byte_array_append(ba, cls.to_byte_array(z))

    @classmethod
    def append_message_to_byte_array(cls, ba: bytearray, message: bytearray):
        cls.byte_array_append(ba, message)

    @classmethod
    def byte_array_to_coordinates(cls, ba: bytearray, offset: int):
        points = []
        for x in range(0, 3):
            decimal_array = bytearray(7)
            for y in range(0, 7):
                decimal_array[y] = ba[y + x * 7 + offset]
            points.append(cls.byte_array_to_decimal(decimal_array))
        return points

    @classmethod
    def byte_array_append(cls, ba: bytearray, other: bytearray):
        for b in other:
            ba.append(b)

    @classmethod
    def byte_array_to_decimal(cls, ba: bytearray):
        return struct.unpack(">L", ba)[0]





