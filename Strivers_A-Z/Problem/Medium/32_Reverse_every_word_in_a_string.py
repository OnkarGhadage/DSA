class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s) - 1
        result = ""
        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue
            
            end = i

            while i >= 0 and s[i] != " ":
                i -= 1
            
            word = s[i + 1 : end + 1]
            if word != "":
                word += " "
            
            result += word
        return result[:-1]