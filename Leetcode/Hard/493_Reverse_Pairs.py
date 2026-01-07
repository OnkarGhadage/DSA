class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def mergesort(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2

            left, lcount = mergesort(arr[:mid])
            right, rcount = mergesort(arr[mid:])

            j = 0
            count = lcount + rcount

            for num in left:
                while j < len(right) and num > 2 * right[j]:
                    j += 1
                count += j 
            
            merged = []

            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, count
        
        _, count = mergesort(nums)

        return count
        