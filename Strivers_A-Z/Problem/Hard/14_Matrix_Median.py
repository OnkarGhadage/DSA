class Solution:
    def findMedian(self, matrix):
        n, m = len(matrix), len(matrix[0])
        total_ele = m * n
        low = matrix[0][0]
        for i in range(1, len(matrix)):
            if low > matrix[i][0]:
                low = matrix[i][0]
        high = matrix[0][m-1]
        for i in range(1, len(matrix)):
            if high < matrix[i][m-1]:
                high = matrix[i][m-1]

        while low <= high:
            mid = (low + high) // 2

            count = self.count_less(matrix, mid)

            if count <= total_ele // 2:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
    
    def count_less(self, matrix, mid):
        count = 0
        for i in range(len(matrix)):
            low, high = 0, len(matrix[i]) - 1
            while low <= high:
                rmid = (low + high) // 2
                if matrix[i][rmid] <= mid:
                    low = rmid + 1 
                else:
                    high = rmid - 1
            count += low
        return count