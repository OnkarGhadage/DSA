class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        low, high = 0, len(mat[0]) - 1
        while low <= high:
            col = (low + high) // 2

            row = self.find_row(mat, col)

            left = mat[row][col - 1] if col > 0 else -1
            right = mat[row][col + 1] if col < len(mat[0]) - 1 else -1

            if mat[row][col] > left and mat[row][col] > right:
                return [row, col]
            elif mat[row][col] < left:
                high = col - 1
            else:
                low = col + 1
    
    def find_row(self, mat, col):
        row = 0
        for i in range(1, len(mat)):
            if mat[row][col] < mat[i][col]:
                row = i
        return row