# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
list_a = []
list_length = (int(input("Please input a length of our list")))
for i in range(list_length):
    el = (int(input(f"Now please input {i + 1} element")))
    list_a.append(el)
    i += 1
print(list_a)
if list_length == 0:
    print(f"element {list_length} don't match the amount")
else:
    x = list_a[(len(list_a)) - 1]
    min_el = (x - list_a[0])
    index = 0
    for i in range(1, list_length):
        count = (x - list_a[i])
        if count < min_el:
            min_el = count
            index = i
    print(
        f"Number {list_a[index]} in list A is nearest number to"
        f" number {x},their difference is {abs(x - list_a[index])}")
