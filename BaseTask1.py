# Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся
# пользователем. После выполнения вычисления программа не должна
# завершаться  а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве
# знака операции.Если пользователь вводит неверный
# знак (не '0', '+', '-', '*', '/'), то программа должнасообщать ему об
# ошибке и снова запрашивать знак операции. Также сообщать пользователю о
# невозможности деления на ноль, если он ввел 0 в качестве делителя.


def func_selector(a, b):
    compute_type = input("Please input a type of compute do you like: ")
    if compute_type == '0':
        return print("End of calculation")
    elif compute_type == '+':
        print(f"result is {a + b}")
        return func_selector(a, b)
    elif compute_type == '-':
        print(f"result is {a - b}")
        return func_selector(a, b)
    elif compute_type == '*':
        if a == 0 or b == 0:
            print("you can't multiply by zero")
            return func_selector(a, b)
        else:
            print(f"result is {a * b}")
    elif compute_type == '/':
        if a == 0 or b == 0:
            print("you can't multiply by zero")
            return func_selector(a, b)
        else:
            print(f"result is {a / b}")
            return func_selector(a, b)
    else:
        print("Please input a correct type of compute")
        return func_selector(a, b)


try:
    a, b = int(input("Input A: ")), int(input("Input B: "))
    func_res = func_selector(a, b)
except ValueError:
    print("Please input an integer number ")
