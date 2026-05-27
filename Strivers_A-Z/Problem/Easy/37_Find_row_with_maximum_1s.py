class Solution:
    def rowWithMax1s(self, mat):
        row = -1
        max_ones_count = 0
        for i in range(len(mat)):
            low, high = 0, len(mat[0]) - 1
            while low <= high:
                mid = (low + high) // 2
                if mat[i][mid] == 1:
                    high = mid - 1
                else:
                    low = mid + 1
            current_count = len(mat[i]) - low
            row = i if current_count > max_ones_count else row
            max_ones_count = max(max_ones_count, current_count)
        return row
