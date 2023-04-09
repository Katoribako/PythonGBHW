# Подсчитать четные и нечетные цифры введенного натурального числа.


def even_selector(num, even=0, not_even=0):
    if num == 0:
        print(f"({even} is count of even elements, {not_even} is"
              f" count of not even elements )")
    else:
        current_num = num % 10
        num = num // 10
        if current_num % 2 == 0:
            even += 1
        else:
            not_even += 1
        return even_selector(num, even, not_even)


try:
    n = abs(int(input("Please input a number: ")))
    even_selector(n)
except ValueError:
    print("Please input an integer number")
