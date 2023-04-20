"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

first_key = ['version 1', 'version 2', 'version 3', 'version 4']
second_key = 5
third_key = {
    'first_value': '1200' + u'\u23EC',
    'second_value': '2000' + u'\u23EC',
    'third_value': '3200' + u'\u23EC',
}

yaml_date = {'first_key': first_key, 'second_key': second_key,
             'third_key': third_key}

with open('result.yaml', 'w', encoding='utf-8') as result_list:
    yaml.dump(yaml_date, result_list, allow_unicode=True,
              default_flow_style=False, default_style='"')

with open('result.yaml', 'r', encoding='utf-8') as file_read:
    print(yaml.safe_load(file_read) == yaml_date)
