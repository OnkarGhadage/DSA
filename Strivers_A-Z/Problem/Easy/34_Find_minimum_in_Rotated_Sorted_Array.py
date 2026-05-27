class Solution:
    def findMin(self, arr):
        low, high = 0, len(arr) - 1
        minimum = arr[0]

        while low <= high:
            mid = (low + high) // 2

            if arr[low] <= arr[mid]:
                minimum = min(minimum, arr[low])
                low = mid + 1
            else:
                minimum = min(minimum, arr[mid])
                high = mid - 1
        
        return minimum