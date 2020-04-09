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