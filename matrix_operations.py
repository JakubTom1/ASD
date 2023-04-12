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

if __name__ == "__main__":
    m = Matrix(
        [[1, 0, 2],
         [-1, 3, 1]]
    )
    m1 = Matrix(
        [[1, 1, 1],
         [1, 1, 1]]
    )
    m2 = Matrix(
        [[3, 1],
         [2, 1],
         [1, 0]]
    )

    print(m+m1, '\n')
    print(m*m2, '\n')
    print(transposed(m))

