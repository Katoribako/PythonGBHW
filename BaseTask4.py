# Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ... Количество элементов (n) вводится с клавиатуры.

def element_sum(num, sum_el=float(0), summator=float(1), count=0):
    if num == 0:
        exit(f"{sum_el} the sum of elements")
    else:
        if count % 2 == 0:
            sum_el = sum_el + summator / 2
            count += 1
            return element_sum(num - 1, sum_el, summator, count)
        else:
            sum_el = sum_el + (summator / 2) * -1
            count += 1
            return element_sum(num - 1, sum_el, summator, count)


try:
    number = abs(int(input("Please input a number of elements ")))
    summ = element_sum(number, sum_el=float(0), summator=float(1), count=0)
except ValueError:
    print("please input an integer number of elements")
