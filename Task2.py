"""
Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
(не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

import binascii


def list_info_descripter(lst):
    print([(el, type(el), binascii.hexlify(el), len(el)) for el in
           lst])


byte_word_array = [b"class", b"function", b"method"]
list_info_descripter(byte_word_array)
