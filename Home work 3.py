class Matrix:
    ''' initials Matrix  '''

    def __init__(self, mat):
        self.matrix = mat

    # used list comprehension for ease and reduced number of lines used
    def matrixForm(self):
        mat = self.matrix
        m = "[" + '\n'.join([str(row) for row in mat]) + "]"
        return m

    def add(self, other):
        mat1 = self.matrix
        mat2 = other.matrix
        Sum = [[mat1[i][j] + mat1[i][j] for j in range(3)]
               for i in range(3)]
        return Matrix(Sum)

    def sub(self, other):
        mat1 = self.matrix
        mat2 = other.matrix
        Sub = [[mat1[i][j] - mat1[i][j] for j in range(3)]
               for i in range(3)]
        return Matrix(Sub)

    # item Multiply
    def multiItem(self, other):
        mat1 = self.matrix
        mat2 = other.matrix
        mul = [[mat1[i][j] * mat1[i][j] for j in range(3)]
               for i in range(3)]
        return Matrix(mul)

    # Matrix Multiply
    def __mul__(self, other):
        mat1 = self.matrix
        mat2 = self.matrix
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                for n in range(3):
                    result[i][j] += mat1[i][n] * mat2[n][j]
        return Matrix(result)

    def det(self):
        mat = self.matrix
        dete = (mat[0][0] * (mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2])
                - mat[1][0] * (mat[0][1] * mat[2][2] - mat[2][1] * mat[0][2])
                + mat[2][0] * (mat[0][1] * mat[1][2] - mat[1][1] * mat[0][2]))
        if dete == 0:
            print(dete, "the Matrix is SINGLE MATRIX")
        else:
            print(dete)


m1 = Matrix([[1, 15, 3], [4, 5, 6], [7, 8, 9]])
# print(m1.matrixForm())

m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# m3 = m2.sub(m1
m3 = m2 * m1
print(m3.matrixForm())

d = m1.det()
print(d)
