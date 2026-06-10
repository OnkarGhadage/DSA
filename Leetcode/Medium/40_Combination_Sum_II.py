# First solution
class Solution:
    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:
        def helper(i, target):
            #Base case
            if target == 0:
                result.append(combination[:])
                return 
            if i >= len(nums) or target < 0:
                return

            #Recursion
            combination.append(nums[i])
            helper(i+1, target-nums[i])

            combination.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, target)
        
        nums.sort()
        result = []
        combination = []
        helper(0, target)
        return result


# Optimized solution
class Solution:
    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:
        def helper(idx, target):
            #Base case
            if target == 0:
                result.append(combination[:])
                return 
            
            for i in range(idx, len(nums)):
                #skip duplicate
                if i > idx and nums[i] == nums[i-1]:
                    continue
                
                if nums[i] > target:
                    break
                
                combination.append(nums[i])
                helper(i+1, target-nums[i])
                combination.pop()
        
        nums.sort()
        result = []
        combination = []
        helper(0, target)
        return result