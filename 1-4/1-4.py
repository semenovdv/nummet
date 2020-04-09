import csv
import numpy as np
from copy import copy
from functools import reduce

"""
    Найти СЗ и СВ матрицы (симметрической)
    Реализовать метод вращений Якоби
    зависимость погрешности от кол-ва итераций
"""

if __name__ == '__main__':
    with open('m.csv', newline='') as mfile:
        matrix = None
        vector = []

        matr_reader = csv.reader(mfile, delimiter=' ')
        for line in matr_reader:
            if matrix is None:
                line = np.array([float(x) for x in line])
                matrix = np.array(line)
            else:
                line = np.array([float(x) for x in line])
                matrix = np.vstack([matrix, line])

        print(matrix)

        U_m = list()

        for _ in range(10):

            max_el = (None, None, None)

            for i, line in enumerate(matrix):
                for j, el in enumerate(line[i+1:]):
                    if max_el[0] is None or abs(max_el[0]) < abs(el):
                        max_el = (el, i, j+i+1)

            #print(max_el)
            i = max_el[1]
            j = max_el[2]
            max_el = max_el[0]

            phi = 0.5*np.arctan((2*max_el)/(matrix[i][i] - matrix[j][j]),)
            U = np.array([[1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]] ,dtype=float)

            c = np.cos(phi)
            U[i][i] = np.cos(phi)
            U[i][j] = -np.sin(phi)
            U[j][i] = np.sin(phi)
            U[j][j] = np.cos(phi)

            U_m.append(U)


            matrix = np.dot(np.dot(np.transpose(U), matrix), U)

        print(matrix.round((2)))

        U_m = reduce(lambda x, y: np.dot(x, y), U_m)

        print(U_m)
        print()
        print(np.round(np.dot(U_m[0], U_m[1])))
        print(np.round(np.dot(U_m[1], U_m[2])))
        print(np.round(np.dot(U_m[0], U_m[2])))








