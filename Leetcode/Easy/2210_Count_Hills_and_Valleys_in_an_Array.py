class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        arr = [nums[0]]
        for i in nums[1:]:
            if arr[-1] != i:
                arr.append(i)
        
        count = 0
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                count += 1
            elif arr[i - 1] > arr[i] < arr[i + 1]:
                count += 1
        
        return count