'''
Реализовать дескрипторы для любых двух классов
'''


class TrueNum:
    def __set_name__(self, owner, parameter):
        self.parameter = parameter

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Please input an integer number that bigger than"
                             " zero")
        if value % 1 != 0:
            raise ValueError("Please input an integer number that bigger than"
                             " zero")
        instance.__dict__[self.parameter] = value


class House:
    _floors_num = TrueNum()
    _apart_per_floor = TrueNum()

    def __init__(self, num_of_floors, apart_per_floor):
        self._floors_num = num_of_floors
        self._apart_per_floor = apart_per_floor

    def apart_amount(self):
        amount = self._floors_num * self._apart_per_floor
        return amount


house_1 = House(7, 7)
print(f"Amount of apartaments in this house is {house_1.apart_amount()}")
