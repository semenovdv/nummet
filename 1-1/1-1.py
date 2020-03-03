from Matrix import Matrix
from Matrix import Vector
from copy import deepcopy
import csv
import numpy

a = "[8.0 4.000000000000001 8.000000000000002 -5.0] matrix det: -2376.0"


if __name__ == '__main__':
    with open('m.csv', newline='') as mfile, \
        open('b.csv', newline='') as vfile:

        matrix = None
        vector = []

        matr_reader = csv.reader(mfile, delimiter=' ')
        for line in matr_reader:
            print(line)
            line = [float(x) for x in line]
            if matrix is None:
                matrix = [line]
            else:
                matrix.append(line)
        matrix = Matrix(matrix)

        vect_reader = csv.reader(vfile, delimiter=' ')
        for line in vect_reader:
            line = [float(x) for x in line]
            vector = line
        vector = Vector(vector)

        print("Matrix: ")
        print(matrix)
        print('Vector: ')
        print(vector)

        LU, P = matrix.lu_decompose()
        
        print('LU matrix: ')
        print(LU)


        print('solving: ')
        print(matrix.lu_solve(LU, P, vector))

        print('matrix det:')
        print(matrix.lu_det(LU))

        print('check ^-1:')
        matrixT = deepcopy(matrix)
        matrixT = matrixT.lu_inverse(LU, P)

        print(matrix * matrixT)

  