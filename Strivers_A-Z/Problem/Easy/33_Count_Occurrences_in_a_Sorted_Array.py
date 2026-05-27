class Solution:
    def countOccurrences(self, arr, target):
        first, last = -1, -1

        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                first = mid
                high = mid - 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                last = mid
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if first == -1:
            return 0
        
        return last - first + 1
