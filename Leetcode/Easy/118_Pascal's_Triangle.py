class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows==1:
            return [[1]]
        triangle = [[1], [1, 1]]
        for i in range(numRows-2):
            new_row = [1, ]
            for j in range(len(triangle[-1])-1):
                new_row.append(triangle[-1][j] + triangle[-1][j+1])
            new_row.append(1)
            triangle.append(new_row)
        return triangle