from abc import ABC, abstractclassmethod

class UIControl(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(controls):
    for control in controls:
        control.draw()


class InvalidOperationError(Exception):
    #derive class from exception class
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is opened")
        self.opened = True
    
    def close(self):
        if self.closed:
            raise InvalidOperationError("Stream is closed")
        self.opened = False

    @abstractclassmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a stream ")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory stream")

stream = MemoryStream()
stream.open()

ddl = DropDownList()
print(isinstance(ddl, UIControl))
#draw(ddl)

tb = TextBox()
print(isinstance(tb, UIControl))
#draw(tb)

draw([ddl, tb])