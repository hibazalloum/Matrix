class Matrix:

    def __init__(self, mat):
        self.matrix = mat

    def matrixForm(self):
        mat = self.matrix
        m = "[" + '\n'.join([str(row) for row in mat]) + "]"
        return m


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m1.matrixForm())
