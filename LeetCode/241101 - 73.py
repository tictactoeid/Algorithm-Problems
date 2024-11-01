# Set Matrix Zeros
# Medium

class Solution:
    def setZeroes_python(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for row in range(m):
                        if matrix[row][j] != 0:
                            matrix[row][j] = None
                    for col in range(n):
                        if matrix[i][col] != 0:
                            matrix[i][col] = None

        for i in range(m):
            for j in range(n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0

    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        row_0 = False
        col_0 = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        row_0 = True
                    if j == 0:
                        col_0 = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            if row_0:
                for j in range(n):
                    matrix[0][j] = 0
            if col_0:
                for i in range(m):
                    matrix[i][0] = 0
                    