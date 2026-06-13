class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(i, k, n, combination):
            #Base case
            if len(combination) == k and n == 0:
                result.append(combination[:])
                return
            if len(combination) >= k or n < 0 or i > 8:
                return

            #Main
            combination.append(l[i])
            helper(i+1, k, n-l[i], combination)

            combination.pop()
            helper(i+1, k, n, combination)
        
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        combination = []
        result = []
        helper(0, k, n, combination)
        return result
    


# Better solution
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(start, target):
            #base case
            if len(combination) == k:
                if target == 0:
                    result.append(combination[:])
                return

            #main
            for i in range(start, 10):
                if i > target:
                    break
                
                combination.append(i)
                helper(i+1, target-i)
                combination.pop()
        
        result = []
        combination = []
        helper(1, n)
        return result