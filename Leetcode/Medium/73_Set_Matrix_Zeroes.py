class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, column = len(matrix), len(matrix[0])
        first_row = False
        first_column = False

        for i in range(column):
            if matrix[0][i] == 0:
                first_row = True
        for i in range(row):

            if matrix[i][0] == 0:
                first_column = True

        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, column):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if first_row:
            for i in range(column):
                matrix[0][i] = 0

        if first_column:
            for i in range(row):
                matrix[i][0] = 0