class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, subset):
            #Base case
            if i >= len(nums):
                result.append(subset[:])
                return
            #Main
            subset.append(nums[i])
            helper(i+1, subset)
            subset.pop()
            helper(i+1, subset)


        result = []
        subset = []
        helper(0, subset)
        return result