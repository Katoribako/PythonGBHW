# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

class BiggerSizeError(Exception):
    pass


class TooSmallSizeError(Exception):
    pass

class SmallSliceError(Exception):
    pass

try:
    n, m, k = int(input("Please input a height of chocolate bar")), \
        int(input("Please input a width of chocolate bar")), \
        int(input("No please input how much a slices of chocolate do you want"
                  ""))
    if k >= n * m:
        raise BiggerSizeError()
    if n <= 1 or m <= 1:
        raise TooSmallSizeError()
    if k <= 1:
        raise SmallSliceError()
except SmallSliceError:
    print("This slice is too small please input a bigger slice")
except ValueError:
    print("You input a incorrect value, please use integer numbers for input")
except TooSmallSizeError:
    print("each side of chocolate bar can be only bigger than 1")
except BiggerSizeError:
    print("A quantity of slices of chocolate bar cannot be equal or bigger"
          " than square area of chocolate bar")
else:
    if k // n or k // m:
        print(f"{k} slices of chocolate can be broken on in a straight line")
    else:
        print(f"{k} slices of chocolate cannot be broken in a straight line")
