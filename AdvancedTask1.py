# Требуется вычислить, сколько раз встречается некоторое число X в массиве
# A[1..N]. Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве.  В последующих  строках записаны
# N целых чисел Ai. Последняя строка содержит число X


def list_generator(base_list):
    list_length = (int(input("Please input a length of our list")))
    for i in range(list_length):
        el = (int(input(f"Now please input {i + 1} element")))
        base_list.append(el)
        i += 1
    return base_list


a_list = []
a_list = list_generator((a_list))
print(a_list)
end_index = a_list[(len(a_list)) - 1]
print(f" A count of {end_index} is "
      f"{a_list.count(end_index)} ")
