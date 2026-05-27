class Solution:
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            while arr[i] < arr[i-1] and i > 0:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                i -= 1

    def recursive_insertion_sort(self, arr, i):
        if i == len(arr) - 1:
            return
        while arr[i] < arr[i-1] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
        self.recursive_insertion_sort(arr, i+1)


s1 = Solution()
arr = [9,3,7,8,1,6,2,4,5]
s1.recursive_insertion_sort(arr,1)
print(arr)