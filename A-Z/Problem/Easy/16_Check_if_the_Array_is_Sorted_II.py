class Solution:
    def isSorted(self, arr) -> bool:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

s1 = Solution()
print(s1.isSorted([1,2,3,4]))
print(s1.isSorted([1, 2, 3, 5, 5, 7, 7, 7, 8, 12, 13, 15, 15, 15, 19]))