#skończone

class Matrix:
    def __init__(self, entrance_value, parameter=0):
        if isinstance(entrance_value, tuple):
            row, col = entrance_value
            matrix = [[parameter for j in range(col)] for i in range(row)]
            self.matrix = matrix
        else:
            self.matrix = entrance_value

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __str__(self):
        output = []
        for row in self.matrix:
            output.append(' '.join([str(col) for col in row]))
        return '|' + '|\n|'.join(output)+ '|'

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other):
        if self.size() == other.size():
            r, c = self.size()
            added_matrix = Matrix((r, c))
            for i in range(r):
                for j in range(c):
                    added_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

            return added_matrix
        else:
            print("Macierze są różnych rozmiarów")
            return None

    def __mul__(self, other):
        if self.size()[1] == other.size()[0]:
            m, n = self.size()
            n, p = other.size()
            multiplied_matrix = Matrix((m, p))
            for i in range(m):
                for j in range(p):
                    sum = 0
                    for k in range(n):
                        sum = sum + self.matrix[i][k] * other.matrix[k][j]
                        multiplied_matrix[i][j] = sum
            return multiplied_matrix
        else:
            print("Rozmiary macierzy są niezgodne z warunkami mnożenia macierzy")
            return None


def transposed(matrix):
    row, col = matrix.size()
    transposed_matrix = Matrix((col, row))
    for i in range(row):
        for j in range(col):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

def determinant(matrix, parameter=1):
    if matrix.size()[0] == matrix.size()[1]:
        n = matrix.size()[0]
        if n > 1:
            det_matrix = Matrix((n-1, n-1))
            matrix_2_dim = Matrix((2, 2))
            idx_of_row = 0
            while matrix[0][0] == 0:
                if idx_of_row < n-1:
                    idx_of_row += 1
                    parameter = parameter * (-1)
                else:
                    return 0
                matrix[0][:], matrix[idx_of_row][:] = matrix[idx_of_row][:], matrix[0][:]

            matrix_2_dim[0][0] = matrix[0][0]
            for row in range(n-1):
                matrix_2_dim[1][0] = matrix[row + 1][0]
                for col in range(n-1):
                    matrix_2_dim[0][1] = matrix[0][col + 1]
                    matrix_2_dim[1][1] = matrix[row + 1][col + 1]
                    det_in_2_dim = matrix_2_dim[0][0] * matrix_2_dim[1][1] - matrix_2_dim[0][1] * matrix_2_dim[1][0]
                    det_matrix[row][col] = det_in_2_dim
            parameter = 1/(matrix[0][0]**(n-2)) * parameter
            return determinant(det_matrix, parameter)
        else:
            return parameter * matrix[0][0]
    else:
        print("Macierz ma błędny wymiar")
        return None

if __name__ == "__main__":
    m = Matrix(
        [
            [5, 1, 1, 2, 3],
            [4, 2, 1, 7, 3],
            [2, 1, 2, 4, 7],
            [9, 1, 0, 7, 0],
            [1, 4, 7, 2, 2]
        ]
    )
    m2 = Matrix([
     [0, 1, 1, 2, 3],
     [4, 2, 1, 7, 3],
     [2, 1, 2, 4, 7],
     [9, 1, 0, 7, 0],
     [1, 4, 7, 2, 2]
    ]
    )
    print(determinant(m))
    print(determinant(m2))