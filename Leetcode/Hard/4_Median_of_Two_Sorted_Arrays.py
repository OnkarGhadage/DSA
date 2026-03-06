class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i, j = 0, 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        n = len(merged)

        if n % 2 == 0:
            return (merged[n//2] + merged[n//2-1]) / 2
        else:
            return merged[n//2]

### Binary Search Approach

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        low, high = 0, len(nums1)
        n, m = len(nums1), len(nums2)
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (n + m + 1) // 2 - cut1

            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]

            r1 = float('inf') if cut1 == n else nums1[cut1]
            r2 = float('inf') if cut2 == m else nums2[cut2]

            if l1 <= r2 and l2 <= r1:
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1