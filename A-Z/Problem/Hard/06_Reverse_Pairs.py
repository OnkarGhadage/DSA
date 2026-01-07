class Solution:
    def reversePairs(self, nums):
        def mergesort(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2

            left, lcount = mergesort(arr[:mid])
            right, rcount = mergesort(arr[mid:])

            merged_arr = []
            i = j = 0
            count = lcount + rcount


            for num in left:
                while j < len(right) and num > 2 * right[j]:
                    j += 1
                count += j

            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged_arr.append(left[i])
                    i += 1
                else:
                    merged_arr.append(right[j])
                    j += 1
            

            merged_arr.extend(left[i:])
            merged_arr.extend(right[j:])

            return merged_arr,count
        
        _, count = mergesort(nums)

        return count
