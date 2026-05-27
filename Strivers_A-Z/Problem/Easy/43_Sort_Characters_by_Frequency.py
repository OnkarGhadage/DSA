from collections import defaultdict
from collections import Counter
class Solution:
    def frequencySort(self, s):
        #your code goes here
        count = defaultdict(int)
        count = Counter(s)
        chars = sorted(count, key=lambda x : count[x], reverse=True)
        result = ""
        for i in chars:
            result += i * count[i]
        return result