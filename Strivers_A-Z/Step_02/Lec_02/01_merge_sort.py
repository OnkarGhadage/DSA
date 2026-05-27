class Solution:
    def divide(self, arr, low, high):
        if low == high:
            return
        mid = (low+high)//2
        self.divide(arr, low, mid)
        self.divide(arr, mid+1, high)
        self.merge(arr, low, mid, high)
    
    def merge(self, arr, low, mid, high):
        temp = []
        l = low
        r = mid+1
        while l <= mid and r <= high:
            if arr[l] <= arr[r]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[r])
                r += 1
        while l <= mid:
            temp.append(arr[l])
            l += 1
        while r <= high:
            temp.append(arr[r])
            r += 1

        for i in range(low, high+1):
            arr[i] = temp[i-low]

    def merge_sort(self, arr):
        self.divide(arr, 0, len(arr)-1)

s1 = Solution()
arr = [9,7,6,3,8,4,1]
print(arr)
s1.merge_sort(arr)
print(arr)