class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        def helper(i, target):
            #Base cases
            if target == 0:
                result.append(combination[:])
                return
            if i >= len(arr) or target < 0:
                return

            #take and stay
            combination.append(arr[i])
            helper(i, target-arr[i])

            combination.pop()
            helper(i+1, target)

        
        result = []
        combination = []

        helper(0, target)
        return result