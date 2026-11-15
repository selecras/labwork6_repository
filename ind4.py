from random import randint


def check_matrix(matrix: list | tuple):
    if not matrix or not matrix[0]:
        raise ValueError("Матрица не может быть пустой")

    example = len(matrix[0])

    for row in matrix:
        if not isinstance(row, (list, tuple)):
            raise ValueError("Некорректная строка матрицы")

        if len(row) != example:
            raise ValueError("Список не является матрицей")


def random_matrix(x: int, y: int, a: int, b: int) -> list:
    if not (x > 0 and y > 0 and a <= b):
        raise ValueError("Некорректные аргументы")
    result = [[randint(a, b) for _ in range(y)] for _ in range(x)]
    return result


def matrix_multiplication(matrix1: list | tuple, matrix2: list | tuple) -> list:
    check_matrix(matrix1)
    check_matrix(matrix2)
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Матрицы перемножить нельзя")

    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix2[0])):
            temp = 0
            for t in range(len(matrix2)):
                temp += matrix1[i][t] * matrix2[t][j]
            result[i].append(temp)
    return result


def matrix_subtraction(matrix1: list | tuple, matrix2: list | tuple) -> list:
    check_matrix(matrix1)
    check_matrix(matrix2)
    matrix2 = [list(map(lambda x: -x, row)) for row in matrix2]
    return matrix_addition(matrix1, matrix2)


def matrix_addition(matrix1: list | tuple, matrix2: list | tuple) -> list:
    check_matrix(matrix1)
    check_matrix(matrix2)
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы нельзя сложить")

    result = []
    for i in range(len(matrix1)):
        row1 = matrix1[i]
        row2 = matrix2[i]
        result.append([row1[t] + row2[t] for t in range(len(row1))])
    return result


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

    multi = matrix_multiplication(a, b)
    add = matrix_addition(a, b)
    sub = matrix_subtraction(a, b)

    print("Умножение:")
    for i in multi:
        print(*i)

    print("\nСложение:")
    for i in add:
        print(*i)

    print("\nВычитание:")
    for i in sub:
        print(*i)
