# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
# "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать публичные методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные,проверить значения атрибутов, вызвать методы
# экземпляров).
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
# str(self) - вызывается функциями str, print и format. Возвращает строковое
# представление объекта.

class Worker():
    def __init__(self, name, surname, position, wage: float = 0,
                 bonus: float = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def full_name(self):
        return print(f'User: {self.name} {self.surname} ')

    def total_income(self):
        return round(sum(self._income.values()), 2)


user1 = Position('Mike', 'Shinoda', 'Siner', 35552.67, 12334.88)
user2 = Position('Sid', 'Mayer', 'Game Dev', 3500034.89, 109999.88)
print(user1.full_name())
print(f'Total income: {user1.total_income()}')
print(user1._income)
print(user2.full_name())
print(f'Total income: {user2.total_income()}')
print(user2.position)
