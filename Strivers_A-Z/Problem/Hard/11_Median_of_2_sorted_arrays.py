class Solution:
    def median(self, arr1, arr2):
        # merge two arrays
        i, j = 0, 0
        n, m = len(arr1), len(arr2)
        merged = []

        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])

        # median
        l = len(merged)

        if l % 2 == 0:
            return (merged[l//2] + merged[l//2-1]) / 2
        else:
            return merged[l//2]