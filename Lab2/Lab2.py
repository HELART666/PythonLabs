import os
import numpy
import numpy as np

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

matrix = np.random.randint(int(input("Введите начало интервала: ")), int(input("Введите конец интервала: ")),
                           size=(n, m))


def result(matrix):
    max_in_strings = matrix.max(1)
    matrix_list = matrix.tolist()
    for x in range(len(matrix_list)):
        for j in range(0, len(matrix_list[x])):
            matrix_list[x][j] = matrix_list[x][j] / max_in_strings[x]
    save(matrix, matrix_list)


def save(input_matrix, new_matrix):
    numpy.savetxt("result1.txt", input_matrix, fmt="%.1d")
    numpy.savetxt("result2.txt", new_matrix, fmt="%.2f")
    open("result.txt", "w").write(open("result1.txt", "r").read() + "\n\n" + open("result2.txt", "r").read())
    os.remove("result1.txt")
    os.remove("result2.txt")
    content = numpy.loadtxt("result.txt")
    return content


result(matrix)
print("\nГотово! Проверьте файл result.txt")