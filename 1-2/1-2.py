from Matrix import TriMatrix, Vector
import csv
import numpy as np

if __name__ == '__main__':
    with open('m.csv', newline='') as mfile,\
    open('b.csv', newline='') as vfile:
        matrix = None
        vector = []

        matr_reader = csv.reader(mfile, delimiter=' ')
        for line in matr_reader:
            if matrix is None:
                line = [0] + line
                line = np.array([float(x) for x in line])
                matrix = np.array(line)
            else:
                if len(line) == 2:
                    line = line + [0]
                line = np.array([float(x) for x in line])
                matrix = np.vstack([matrix, line])


        print(matrix)
        print('ok')


        vect_reader = csv.reader(vfile, delimiter=' ')
        for line in vect_reader:
            vector = np.array([float(x) for x in line])
            
        print(vector)
        print('ok')
        
        P = np.array([-matrix[0][2]] / matrix[0][1])
        Q = np.array([vector[0] / matrix[0][1]])
        
        for i in range(1, len(matrix)):
            P = np.append(P, -matrix[i][2]/(matrix[i][1] + matrix[i][0]*P[P.size-1]))
            Q = np.append(Q, (vector[i] - matrix[i][0]*Q[Q.size-1]) /(matrix[i][1]+matrix[i][0]*P[P.size-2]))

        
        x_rev = np.array([Q[Q.size-1]])
        j = 1
        for i in range(len(matrix), 0, -1):
            x_rev = np.append(x_rev, P[P.size-j] * x_rev[x_rev.size-1] + Q[Q.size-j])
            j+=1
            
        print(x_rev[::-1][:-1])



   
