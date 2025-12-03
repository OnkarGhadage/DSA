class Solution:

    def quick_sort(self, arr, low, high):
        if low < high:
            pivot_place = self.conquer(arr, low, high)
            self.quick_sort(arr, low, pivot_place-1)
            self.quick_sort(arr, pivot_place+1, high)

    def conquer(self, arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while i <= j:
            while i <= high and arr[i] <= pivot:
                i += 1
            while j > low and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] =  arr[j], arr[low]
        return j

s1 = Solution()
arr = [9,8,7,6,5,4,3,2,1]
print(arr)
s1.quick_sort(arr, 0, len(arr)-1)
print(arr)
