import Encryptor
import Decryptor
import SphereCryptor
from Point import Point
from Vector import Vector
from appJar import gui
import pyperclip


# encrypted = Encryptor.encrypt("hello", 16)
# print(encrypted)
# decrypted = Decryptor.decrypt(encrypted)
# print(decrypted)


# handle button events
def press(button):
    text = app.getEntry("Text")
    difficulty = app.getEntry("Difficulty")
    if button == "Encode":
        encrypt = Encryptor.encrypt(text, int(difficulty))
        pyperclip.copy(encrypt)
        app.setMessage('Output', encrypt)
    else:
        decrypt = Decryptor.decrypt(text, int(difficulty))
        pyperclip.copy(decrypt)
        app.setMessage('Output', decrypt)


# create a GUI variable called app
app = gui("sphereCrypt", "650x400")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to sphereCrypt")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("Text")
app.addLabelEntry("Difficulty")
app.addMessage("Info", 'Difficulty is any number between two and sixteen. Additionally, '
                       'The output of the encryption / decryption is automatically copied to your clipboard, '
                       'so in order to access the messages just CTRL-V on any text line')
app.setMessageWidth("Info", 650)
app.addEmptyMessage('Output')
app.setMessageWidth('Output', 650)

# link the buttons to the function called press
app.addButtons(["Encode", "Decode"], press)

app.setFocus("Text")

# start the GUI
app.go()
