# Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел (каждый элемент ряда меньше или равен предыдущему).
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

class WrongValue(Exception):
    pass


def value_filter(number):
    try:
        number = int(input("Please input your number"))
        if number <= 0:
            raise WrongValue()
    except WrongValue:
        exit(
            "Please input a correct number (it must be an integer greater than"
            " zero)")
    except ValueError:
        exit(
            "Please input a correct number (it must be an integer greater than"
            " zero)")
    else:
        return number


def list_generator(base_list):
    base_list = []
    list_length = int(input("Please input a length of list"))
    for i in range(list_length):
        el = int(input(f"Please input a {i + 1} element"))
        base_list.append(el)
        i += 1
        base_list = sorted(base_list, reverse=True)
    return base_list


rating_list = []
rating_list = list_generator(rating_list)
print(f"Rating now is {rating_list}")
your_rate = int(value_filter(input()))
num_of_elements = rating_list.count(your_rate)
if num_of_elements == 0:
    rating_list.append(your_rate)
    rating_list = sorted(rating_list, reverse=True)
    print(f"Rating now is {rating_list}")
if num_of_elements > 0:
    el_num = rating_list.index(your_rate)
    rating_list.insert(el_num, your_rate)
    print(f"Rating now is {rating_list}")
