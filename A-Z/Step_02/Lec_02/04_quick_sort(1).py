class Solution:
    def lomuto_partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[i], arr[high] = arr[high], arr[i]

        return i

    def quicksort_lomuto(self, arr, low, high):
        if low < high:
            part_index = self.lomuto_partition(arr, low, high)
            self.quicksort_lomuto(arr, low, part_index - 1)
            self.quicksort_lomuto(arr, part_index + 1, high)

    def hoare_partition(self, arr, low, high):
        pivot = arr[low]
        i, j = low-1, high + 1
        while True:
            i += 1
            while i <= high and arr[i] < pivot:
                i += 1
            j -= 1
            while j >= low and arr[j] > pivot:
                j -= 1
            
            if i >= j:
                return j

            arr[i], arr[j] = arr[j], arr[i]

    def quicksort_hoare(self, arr, low, high):
        if low < high:
            part_index = self.hoare_partition(arr, low, high)
            self.quicksort_hoare(arr, low, part_index)
            self.quicksort_hoare(arr, part_index + 1, high)
