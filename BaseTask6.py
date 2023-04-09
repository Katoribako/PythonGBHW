# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное
# пользователем число, чем то, что загадано. Если за 10 попыток число не
# отгадано,то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

import random


def guess_num(num, tray=0):
    if tray > 10:
        exit(f"you didn't guess: {num} is right number!")
    else:
        try:
            answer = abs(int(input("Please input an integer number: ")))
            if answer > num:
                tray += 1
                print(f"{answer} is bigger than hidden number")
                return guess_num(num, tray)
            if answer < num:
                tray += 1
                print(f"{answer} is smaller than hidden number")
                return guess_num(num, tray)
            else:
                exit(f"You are right! {answer} is a right hidden number!")
        except ValueError:
            print("Please input a correct integer number")
            return guess_num(num)


hidden_num = random.randint(1, 99)
guess_num(hidden_num)

