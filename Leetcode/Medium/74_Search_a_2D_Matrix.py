class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        low, high = 0, n * m - 1

        while low <= high:
            mid = (low + high) // 2
            i, j = mid // m, mid % m

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return False