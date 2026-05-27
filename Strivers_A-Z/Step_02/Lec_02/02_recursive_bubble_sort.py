class Solution:

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n-1):
            swaped = False
            for j in range(n-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaped = True
            if not swaped:
                return
    
    def recursive_bubble_sort(self, arr, n):
        if n == 1:
            return
        swaped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaped = True
        if not swaped:
            return
        
        self.recursive_bubble_sort(arr,n-1)

s1 = Solution()
arr = [9,3,7,8,1,6,2,4,5]
print(arr)
s1.recursive_bubble_sort(arr,len(arr))
print(arr)