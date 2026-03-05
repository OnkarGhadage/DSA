class Solution:
    def paint(self, A: int, B: int, C: list[int]) -> int:
        # Your code goes here
        low, high = max(C) * B, sum(C) * B 
        while low <= high:
            mid = (low + high) // 2

            if self.is_possible(A, B, C, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low % 10000003
    
    def is_possible(self, A, B, C, mid):
        count = 1
        current_sum = 0
        for i in C:
            current = i * B
            if current + current_sum > mid:
                count += 1
                current_sum = current
            else:
                current_sum += current
        return count <= A