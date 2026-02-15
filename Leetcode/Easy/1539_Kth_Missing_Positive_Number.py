class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        i = 0
        j = 1
        no = 0
        missing = 0
        while i < len(arr):
            if arr[i] != j:
                no += 1
                missing = j
                if no == k:
                    return missing
                j += 1
            else:
                i += 1
                j += 1
        return arr[-1] + k - no