# Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в
# каждой строке.

def ascii_table(ascii_num=32):
    if ascii_num == 128:
        return True
    print(f' {ascii_num} - {chr(ascii_num)}', end=' ')
    if (ascii_num - 31) % 10 == 0:
        print('\n')

    ascii_table(ascii_num + 1)


ascii_table()
