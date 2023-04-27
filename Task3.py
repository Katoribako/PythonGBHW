"""
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


def bytes_words(array):
    word_list = []
    try:
        print([(word_list.append(bytes(el, 'ascii'))) for el in array])
    except UnicodeEncodeError:
        print("Not ascii!")
    return word_list


words = ['attribute', 'класс', 'функция', 'type']
print(bytes_words(words))
