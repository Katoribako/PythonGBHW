# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

try:
    print("an = a1 + (n -1) * d")
    a1 = abs(int(input("Please input a1: ")))
    n = abs(int(input("Please input n: ")))
    d = abs(int(input("Please input d: ")))
    print([a1 + el * d for el in range(n)])
except ValueError:
    exit("Please input an integer number")
