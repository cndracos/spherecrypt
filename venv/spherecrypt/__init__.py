import Encryptor
import Decryptor
import SphereCryptor
from Point import Point
from Vector import Vector

encrypted = Encryptor.encrypt("hello", 16)
print(encrypted)
decrypted = Decryptor.decrypt(encrypted)
print(decrypted)
