class Matrix:

    def __init__(self, mat):
        self.matrix = mat

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


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(m1.matrixForm())

m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m3 = m2.add(m1)
print(m3.matrixForm())
