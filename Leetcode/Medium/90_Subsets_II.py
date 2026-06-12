class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i, combination):
            #Base case
            if i >= len(nums):
                result.append(combination[:])
                return

            #Main
            combination.append(nums[i])
            helper(i+1, combination)

            #Skip duplicates
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            combination.pop()
            helper(i+1, combination)

        nums.sort()
        result = []
        combination = []
        helper(0, combination)
        return result