class Solution:
    def unionArray(self, nums1, nums2):
        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1

            elif nums1[i] > nums2[j]:
                if not result or result[-1] != nums2[j]:
                    result.append(nums2[j])
                j += 1

            else:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1

        while i < len(nums1):
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1

        while j < len(nums2):
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1

        return result