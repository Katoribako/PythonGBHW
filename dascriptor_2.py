# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

class NumVerificator:
    def __set_name__(self, owner, my_attr):
        self.parameter = my_attr

    def __set__(self, instance, value):
        if type(value) != int and type(value) != float:
            raise NameError("Please input an integer number that bigger than"
                            " zero")
        if value <= 0:
            raise ValueError("Please input an integer number that bigger than"
                             " zero")
        instance.__dict__[self.parameter] = value


class Road:
    _asph_len = NumVerificator()
    _asph_width = NumVerificator()
    _weight_per_sm = NumVerificator()
    _thickness = NumVerificator()

    def __init__(self, asph_len, asph_width, weight_per_sm, thickness):
        self._asph_len = asph_len
        self._asph_width = asph_width
        self._weight_per_sm = weight_per_sm
        self._thickness = thickness

    def asph_weigth(self):
        thickness = 0.05
        return self._asph_len * self._asph_width * self._thickness \
            * self._weight_per_sm


road1 = Road(12, 20, 20.4, 12)
print(f"weight of road is {road1.asph_weigth()}")
