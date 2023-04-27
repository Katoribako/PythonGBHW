"""
Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' -
набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""


def code_point_generator(array):
    code_point_list = []
    for el in array:
        encode_value = el.encode("unicode_escape", "utf-8")
        code_point_list.append(encode_value.decode("utf-8"))
    return code_point_list


def result_printing(word_list, code_point_list):
    for i in range(len(word_list)):
        print(f'Слово "{word_list[i]}" - буквенный формат. \n Тип данных: '
              f'{type(word_list[i])}')
        print(f'{code_point_list[i]} - набор кодовых точек. \n Тип данных: '
              f'{type(code_point_list[i])} ')


words_list = ['разработка', 'сокет', 'декоратор']
result_printing(words_list, code_point_generator(words_list))
