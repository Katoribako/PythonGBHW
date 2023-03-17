# Найдите сумму цифр трехзначного числа.

class BigValue(Exception):
    pass


try:
    number = int(input("Please input a number "))
    if number > 999 or number < 100:
        raise BigValue()
except ValueError:
    print("Please input correct number")
except BigValue:
    print("Please input correct number")
else:
    a = number // 100
    b = number // 10 % 10
    c = number % 10
    print(f"sum of digits of a three-digit number is {a + b + c}")
