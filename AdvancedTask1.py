# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def rec_round():
    a, b = abs(int(input("Please input A: "))), abs(int(input("Please "
                                                              "input B: ")))
    if a == 0 or b == 0:
        print("Any number to the zero power is equal to one.")
        return 1
    else:
        print(a ** b)
        return rec_round()


try:
    rec_round()
except ValueError:
    print("Please input a correct number")
