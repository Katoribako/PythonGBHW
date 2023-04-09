# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только
# +1 и -1. Также нельзя использовать циклы.

def easy_sum(a, b, c=0):
    if c == a + b:
        print(f"{c} is sum of {a} and {b}")
        return c
    if c < a + b:
        c += 1
        return easy_sum(a, b, c)


try:
    num_a, num_b = abs(int(input("Please input A: "))), \
        abs(int(input("Please input  B: ")))
    easy_sum(num_a, num_b)
except ValueError:
    exit("Please input an integer number ")
