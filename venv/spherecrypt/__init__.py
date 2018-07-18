import random
from Point import *
from Vector import Vector
from SphereCryptor import SphereCryptor
from Encryptor import Encryptor
from Decryptor import Decryptor
from ByteUtilities import *

word = Encryptor.encrypt("hello", 222)
decrypted: bytearray = Decryptor.decrypt(word)
print(decrypted.decode(encoding="utf-8"))

