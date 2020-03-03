from functools import reduce

class MyException(Exception):
    pass


class Vector:
    def __init__(self, data=None):
        if data is None:
            self.data = []
            self.size = 0
        else:
            self.data = data
            self.size = len(data)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        mstr = '['
        for i in range(self.size):
            if i != 0:
                mstr += ' '
            mstr += str(self.data[i])
        return mstr + ']'


class Matrix:
    def __init__(self, data=None, size=None):

        def check_matr(m_data):
            if len(set([len(item) for item in m_data])) == 1:
                return True
            return False

        if data is None and size is None:
            self.size = (1, 1)
            self.data = [[None]]

        elif data is None:
            self.size = size
            tmp_data = []
            for i in range(self.size[0]):
                tmp_data.append([])
                for j in range(self.size[1]):
                    tmp_data[i].append(None)
            self.data = tmp_data

        elif size is None:
            sh0 = len(data)
            sh1 = len(data[0])
            self.size = (sh0, sh1)
            if check_matr(data):
                self.data = data
            else:
                raise MyException('check_matr failed')
        else:
            if check_matr(data):
                if size[0] == len(data) and size[1] == len(data[0]):
                    self.size = size
                    self.data = data
                else:
                    raise MyException('check_matr failed')

        self.LU = None
        self.P = None


    def lu_decompose(self):
        assert self.size[0] == self.size[1]
        size = self.size[0]
        LU = self.data.copy()
        P = Matrix.eye(len(LU))

        # k - эпоха прохода по матрице - ступени
        for k in range(size - 1):
            row = max(range(k, self.size[0]), key=lambda j: abs(LU[j][k]))
            if k != row:
                LU[k], LU[row] = LU[row], LU[k]
                P[k], P[row] = P[row], P[k]
            # j - изменяемые строки
            for j in range(k + 1, size):
                LU[j][k] /= LU[k][k]
                # i - изменяемые столбцы
                for i in range(k + 1, size):
                    LU[j][i] -= LU[j][k] * LU[k][i]
        self.LU = LU
        self.P = P
        return LU, P


    def lu_solve(self, vect):
        assert type(vect) == Vector
        # первая часть Ly = Pb
        Pb = self.P * vect
        y = list([Pb[0]])

        for i in range(1, self.size[0]):
            l = self.LU[i][0:i]
            y.append(Pb[i] - sum(a * b for a, b in zip(y, l)))

        # вторая часть
        x = list([y[self.size[0]-1]/self.LU[self.size[0]-1][self.size[0]-1]])
        for i in range(self.size[0]-2, -1, -1):
            l = self.LU[i][i+1:]
            x.insert(0, (y[i] - sum(a * b for a, b in zip(x, l)))/self.LU[i][i])

        return Vector(x)

    def lu_det(self):
        return reduce(lambda x, y: x * y, [self.LU[i][i] for i in range(self.size[0])])

    def lu_inverse(self):
        E = self.eye(self.size[0])
        x = []
        for row in E:
            x.append(self.lu_solve(row))
        res = Matrix(x)
        res.transpose()
        return res

    def transpose(self):
        pass

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __mul__(self, other):
        if type(other) == Matrix:
            assert self.size[1] == other.size[0]
            # типо транспонирование
            other_T = list(zip(*other.data))
            result = Matrix([[sum(ea * eb for ea, eb in zip(a, b)) for b in other_T] for a in self.data])
            return result
        elif type(other) == Vector:
            assert self.size[0] == other.size
            # типо транспонирование
            #other_T = list(zip(*other.data))

            result = Vector([sum(ea * eb for ea, eb in zip(a,other.data)) for a in self.data])

            return result
        else:
            raise MyException('non correct type')

    def __add__(self, other):
        assert self.size == other.size

        added = [[self.data[i][j] + other.data[i][j] for j in range(self.size[0])] for i in range(self.size[1])]
        return Matrix(added)

    def __sub__(self, other):
        assert self.size == other.size

        subbed = [[self.data[i][j] - other.data[i][j] for j in range(self.size[0])] for i in range(self.size[1])]
        return Matrix(subbed)

    def __repr__(self):

        mstr = '['
        for i in range(self.size[0]):
            if i != 0:
                mstr += ' '
            mstr += '['
            for j in range(self.size[1]):
                mstr += str(self.data[i][j])
                if j != self.size[1] - 1:
                    mstr += ' '
            mstr += ']\n'
        return mstr[:-1] + ']'

    @staticmethod
    def eye(num):
        return Matrix([[1 if i == j else 0 for j in range(num)] for i in range(num)])


a = Matrix([[1, 2, 3], [5, 2, 3], [1, 3, 9]])
b = Matrix([[3, 2, 1], [3, 2, 1], [3, 2, 1]])


print()
a.lu_decompose()
print(a.LU)
print()
print(a.P)
print(a.lu_solve(Vector([1, 2, 3])))
print(a.lu_det())
print()






