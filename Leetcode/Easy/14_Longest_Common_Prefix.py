class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return first[:i]
        return first if len(first) < len(last) else last