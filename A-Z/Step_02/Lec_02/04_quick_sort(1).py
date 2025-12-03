class Solution:
    def quickSort(self, arr, low, high):
        #code here 
        if low < high:
            part_idx = self.partition(arr, low, high)
            self.quickSort(arr, low, part_idx-1)
            self.quickSort(arr, part_idx+1, high)

    def partition(self, arr, low, high):
        #code here
        pivot = arr[high]
        i = low-1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

s1 = Solution()
arr = [9,4,3,8,7,6,1,2,5]
print(arr)
s1.quickSort(arr, 0, len(arr)-1)
print(arr)