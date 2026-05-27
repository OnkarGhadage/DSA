class Solution:    
    def rotateString(self, s, goal):
        for i in range(len(s)):
            temp = s[::-1]
            temp = temp[:i][::-1] + temp[i:][::-1]
            if temp == goal:
                return True
        return False