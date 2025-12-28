class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        num1, num2 = None, None
        count1, count2 = 0, 0
        for i in nums:
            if i == num1:
                count1 += 1
            elif i == num2:
                count2 += 1
            elif count1 == 0:
                num1 = i
                count1 = 1
            elif count2 == 0:
                num2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        n = len(nums)//3

        if nums.count(num1) > n:
            result.append(num1)
        if num2 is not None and num2 != num1 and nums.count(num2) > n:
            result.append(num2)
        
        return result
