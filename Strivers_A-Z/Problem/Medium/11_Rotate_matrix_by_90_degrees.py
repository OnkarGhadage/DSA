class Solution:
    def rotateMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i, v in enumerate(matrix):
            matrix[i] = v[::-1]