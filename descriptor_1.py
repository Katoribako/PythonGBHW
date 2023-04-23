# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и
# публичный метод running (запуск).
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class ArrayDetector:
    def __set_name__(self, owner, my_attr):
        self.parameter = my_attr

    def __set__(self, instance, value):
        if type(value) != list:
            raise ValueError("Please input a data with using a lists")
        instance.__dict__[self.parameter] = value


class TrafficLight:
    _color_list = ArrayDetector()
    _waiting_time = ArrayDetector()

    def __init__(self, color_list, waiting_list):
        self._color_list = color_list
        self._waiting_time = waiting_list

    def working_process(self):
        for color, wait in zip(self._color_list, self._waiting_time):
            print(f"{color} цвет будет работать "
                  f"{wait} секунд ")
            time.sleep(int(wait))


tl = TrafficLight(['красный', 'зелёный'], [7, 5])
tl.working_process()
