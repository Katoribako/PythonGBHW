# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

class NegativeNum(Exception):
    pass


class WrongNum(Exception):
    pass


try:
    num = int(input("Please input a number of coins"))
    if num <= 0:
        raise NegativeNum()
except ValueError:
    print("This is not integer number! please input a integer number")
except NegativeNum:
    print("Please input a positive number")
else:
    zero_count = 0
    coin_amount = 0
    for i in range(num):
        try:
            coin = int(input("which side did the coin fall on? "
                             "(heads - 1 / tails - 0)"))
            if coin < 0:
                raise NegativeNum
            if coin != 0 and coin != 1:
                raise WrongNum()
        except WrongNum:
            print("Please input 0 or 1")
            break
        except NegativeNum:
            print("Please input a positive number")
            break
        except ValueError:
            print("Please input 0 or 1")
            break
        else:
            if coin == 0:
                zero_count += 1
        coin_amount = num - zero_count
    print(f"You need a flip coins at least {coin_amount} times")
