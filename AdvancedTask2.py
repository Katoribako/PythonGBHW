# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
# максимума)

try:
    num_list = [-1, 2, 3, 7, 8, 5, 6, 2, -4, -20]
    min_number = int(input())
    max_number = int(input())
    for el in range(len(num_list)):
        if min_number <= num_list[el] <= max_number:
            print(el)
except ValueError:
    exit("Please input an integer number")