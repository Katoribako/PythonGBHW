# Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.

def left_func(num, res=0, sum_c=1):
    if sum_c == num:
        end_sum = res + num
        return end_sum
    else:
        res = res + sum_c
        sum_c += 1
        return left_func(num, res, sum_c)


try:
    num = abs(int(input("Please input a number: ")))
    right_func = num * (num + 1) / 2
    print(f"{left_func(num)} is result of left part of function")
    print(f"{right_func} is result of right part of function")
    if left_func(num) != right_func:
        exit("functions are not equal")
    else:
        exit("Congratulation! functions are equal")
except ValueError:
    exit("You entered are not correct value ")
