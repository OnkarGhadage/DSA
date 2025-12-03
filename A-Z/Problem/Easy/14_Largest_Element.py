class Solution:
    
    def largestElement(self, nums):
        nums.sort()
        return nums[-1]
    
    def largestElement_mannual(self, nums):
        max = nums[0]
        for i in nums:
            if i > max:
                max = i
        return max

s1 = Solution()
print(s1.largestElement([9,2,4,8,6,7,3,1,5]))
print(s1.largestElement_mannual([9,2,4,8,6,7,33,1,5]))