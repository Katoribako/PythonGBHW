"""
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

import chardet

word_array = ['разработка', 'сокет', 'декоратор']
bytes_array = []

for s in word_array:
    s = s.encode('utf-8', errors='namereplace')
    bytes_array.append(s)
    print(s)

for s in bytes_array:
    print(s.decode('ascii', errors='replace'))
    print(s.decode(chardet.detect(s)['encoding']))