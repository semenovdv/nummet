import csv
import numpy as np
from copy import copy


"""
Метод простых итераций и Зейделя

"""



if __name__ == '__main__':
    with open('m.csv', newline='') as mfile, \
            open('v.csv', newline='') as vfile:
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


        vect_reader = csv.reader(vfile, delimiter=' ')
        for line in vect_reader:
            vector = np.array([float(x) for x in line])
        print(matrix,vector)
        for i, row in enumerate(matrix):
            vector[i] = vector[i]/row[i]
            matrix[i] = -row/row[i]
            matrix[i][i] = 0

        print(matrix)

        print(max([sum(abs(i)) for i in matrix]))

        x = copy(vector)
        x_prev = np.array([0, 0, 0, 0])
        while(sum(abs(x-x_prev)) > 0.01):
            x_prev = x
            x = vector + np.matmul(matrix, x)
        print(x)

        # мб Зейделем















