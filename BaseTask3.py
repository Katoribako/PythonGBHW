# Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран.

def reverser(num, el=0):
    if num == 0:
        exit(f" {el} is reversed number")
    else:
        temp = num % 10
        el = el * 10
        el = el + temp
    return reverser(num // 10, el)


try:
    number = abs(int(input("Input a number")))
    print(reverser(number))
except ValueError:
    print("Please input an integer number ")
