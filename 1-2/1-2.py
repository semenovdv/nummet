from Matrix import TriMatrix, Vector

import numpy as np


def tma(mat, D):
    sz = len(mat)
    x = Vector(sz)
    p, q = [], []
    p.append(-mat.c[0] / mat.b[0])
    q.append(D[0] / mat.b[0])

    for i in range(1, sz):
        p_i = 0 if i == sz - 1 else (-mat.c[i] / (mat.b[i] + mat.a[i] * p[i - 1]))
        q_i = (D[i] - mat.a[i] * q[i - 1]) / (mat.b[i] + mat.a[i] * p[i - 1])
        p.append(p_i)
        q.append(q_i)

    x[sz - 1] = q[sz - 1]
    for i in range(sz - 2, -1, -1):
        x[i] = p[i] * x[i + 1] + q[i]

    return x


if __name__ == '__main__':
    with open('m.csv', newline='') as mfile:
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

        matrix[0] = [0] + matrix[0]  
        matrix[-1] = matrix[-1] + [0]      
        matrix = TriMatrix(matrix)
        print(matrix)


        vect_reader = csv.reader(vfile, delimiter=' ')
        for line in vect_reader:
            line = [float(x) for x in line]
            vector = line
        vector = Vector(vector)




    mat, D = TriMatrix(), Vector()
    read_triagonal_matrix(args.input, mat, D)

    logging.info("Input matrix:")
    logging.info(mat)
    logging.info("Input vector:")
    logging.info(D)

    x = tma(mat, D)
    logging.info("Answer:")
    logging.info(x)
    save_to_file(args.output, X=x)