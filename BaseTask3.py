# Реализовать структуру данных «Товары». Она должна представлять собой
# список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные
# у пользователя.
class WrongValue(Exception):
    pass


try:
    amount = int(input("Please input an amount of goods"))
    if amount <= 0:
        raise WrongValue()
except WrongValue:
    print("Please input correct integer that greater than zero")
except ValueError:
    print("Please input correct integer that greater than zero")
else:
    number = 1
    goods = []
    while number <= amount:
        parameters = {}
        while input(f""
                    f"Would you like add {number} product parameters? "
                    "Enter yes/no: ") == 'yes':
            parameter = input("Input type of parameter")
            parameter_value = input("Input a value of parameter ")
            parameters[parameter] = parameter_value
        goods.append(tuple([number, parameters]))
        number += 1
    print(goods)
    analytics = {}
    for product in goods:
        for parameter, parameter_value in product[1].items():
            if parameter in analytics:
                analytics[parameter].append(parameter_value)
            else:
                analytics[parameter] = [parameter_value]
        print(analytics)
