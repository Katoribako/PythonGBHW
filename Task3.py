# Требуется вывести все целые степени двойки (т.е. числа вида 2k)
# , не превосходящие числа N.

class WrongNumber(Exception):
    pass


try:
    number = int(input("Please input a number"))
    if number < 2:
        raise WrongNumber()
except WrongNumber:
    print("Please input a number > 2")
except ValueError:
    print("Please input an integer number")
else:
    j = 0
    while 2 ** j <= number:
        print(2 ** j)
        j += 1
