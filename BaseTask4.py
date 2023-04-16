# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод init()), который должен принимать данные (список списков) для
# формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

class Matrix:
    def __init__(self, matrix_list1, matrix_list2):
        self.matrix_list1 = matrix_list1
        self.matrix_list2 = matrix_list2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.matrix_list1)):

            for j in range(len(self.matrix_list2[i])):
                matr[i][j] = self.matrix_list1[i][j] + self.matrix_list2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


my_matrix = Matrix([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                   [[10, 11, 12],
                    [13, 14, 15],
                    [16, 17, 18]])

print(my_matrix.__add__())