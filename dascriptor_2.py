'''
Реализовать дескрипторы для любых двух классов
'''


class CorrectAttr:
    def __set_name__(self, owner, parameter):
        self.parameter = parameter

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Please input a number is bigger than zero")
        instance.__dict__[self.parameter] = value


class Room:
    _length = CorrectAttr()
    _width = CorrectAttr()
    _height = CorrectAttr()

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def room_square(self):
        square = self._length * self._width * self._height
        return int(square)


room1 = Room(10, 10, 10)
print(f"The square of current room is {room1.room_square()}")
