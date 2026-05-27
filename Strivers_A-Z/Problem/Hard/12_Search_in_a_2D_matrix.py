class Solution:
    def searchMatrix(self, mat, target):
        low, high = 0, len(mat) * len(mat[0]) - 1
        m = len(mat[0])

        while low <= high:
            mid = (low + high) // 2

            i, j = mid // m, mid % m

            if mat[i][j] == target:
                return True
            elif mat[i][j] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False