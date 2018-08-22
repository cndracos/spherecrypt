import struct


def get_message_bytes(ba, offset):
    message = bytearray()
    for x in range(offset, len(ba)):
        message.append(ba[x])
    return message


def to_byte_array(value):
    return bytearray(struct.pack("f", value))


def coordinate_byte_array(ba, x, y, z):
    byte_array_append(ba, to_byte_array(x))
    byte_array_append(ba, to_byte_array(y))
    byte_array_append(ba, to_byte_array(z))


def byte_array_append(ba, message):
    for b in message:
        ba.append(b)


def byte_array_to_coordinates(ba, offset):
    points = []
    for x in range(0, 3):
        decimal_array = bytearray(4)
        for y in range(0, 4):
            decimal_array[y] = ba[y + x * 4 + offset]
        points.append(byte_array_to_decimal(decimal_array))
    return points


def byte_array_to_decimal(ba: bytearray):
    return struct.unpack("f", ba)[0]
