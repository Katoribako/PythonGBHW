"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess


def ping_show(args):
    process_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process_ping.stdout:
        line_detect = chardet.detect(line)['encoding']
        line = line.decode(line_detect).encode('utf-8')
        print(line.decode('utf-8'), end='')


yandex = ['ping', 'yandex.ru']
youtube = ['ping', 'youtube.com']
ping_show(yandex)
ping_show(youtube)