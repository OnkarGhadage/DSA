class Solution:
    def setZeroes(self, matrix):
        # Your code goes here
        row, column = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    column.append(j)
        row = set(row)
        column = set(column)
        for r in row:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0        
        for c in column:
            for j in range(len(matrix)):
                matrix[j][c] = 0
