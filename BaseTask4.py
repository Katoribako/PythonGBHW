# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод init()), который должен принимать данные (список списков) для
# формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
import copy

import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        add_res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                add_res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(add_res)

    def __sub__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        sub_res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                sub_res[i][k] = self.matrix[i][k] - other.matrix[i][k]
        return Matrix(sub_res)

    def __mul__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        mul_res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                mul_res[i][k] = self.matrix[i][k] * other.matrix[i][k]
        return Matrix(mul_res)


l1 = [[1, 2, 4], [3, 4, 5], [5, 6, 6]]
l2 = [[11, 21, 41], [31, 41, 51], [51, 61, 61]]
matr1 = Matrix(l1)
matr2 = Matrix(l2)
print(matr1)
print(matr2)
matr_res = matr1 + matr2
print('result ')
print(matr_res)
matr_z = matr1 - matr2
print(matr_z)
matr_mult = matr1 * matr2
print(matr_mult)
new_matr = matr_z + matr_mult
print(new_matr)
