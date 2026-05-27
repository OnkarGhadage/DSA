class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) * len(grid)
        ori_sum = n*(n+1)//2
        act_sum = 0
        dic = {}
        result = [None, None]
        for i in grid:
            for j in i:
                act_sum += j
                dic[j] = dic.get(j, 0) + 1
                if dic[j] == 2:
                    result[0] = j
        result[1] = ori_sum - (act_sum - result[0])
        return result