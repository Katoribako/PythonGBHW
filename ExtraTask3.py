# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет
# с шестизначным номером, где сумма первых трех цифр равна
# сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6.  Вам требуется написать программу, которая
# проверяет счастливость билета.

class WrongValue(Exception):
    pass


class NoLuckTicket(Exception):
    pass


try:
    ticket = int(input("Please input a number of ticket "))
    if ticket > 999999 or ticket < 100000:
        raise WrongValue()
except ValueError:
    print("Please input a correct number of ticket")
except WrongValue:
    print("Please input a correct number of ticket")
else:
    try:
        first_half = ticket // 1000
        second_half = ticket % 1000
        a = first_half // 100
        b = first_half // 10 % 10
        c = first_half % 10
        first_half_sum = a + b + c
        d = second_half // 100
        e = second_half // 10 % 10
        f = second_half % 10
        second_half_sum = d + e + f
        if first_half_sum != second_half_sum:
            raise NoLuckTicket()
        else:
            print(f"Your ticket {ticket} is lucky ticket! ")
    except NoLuckTicket:
        print(f"Your ticket {ticket} is no luck ticket because sum of left"
              f" half of ticket {first_half_sum} not equal sum of right half"
              f" {second_half_sum}")

