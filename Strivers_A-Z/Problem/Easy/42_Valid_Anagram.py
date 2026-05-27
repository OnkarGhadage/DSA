class Solution:    
    def anagramStrings(self, s, t):
        #your code goes here
        if len(s) != len(t):
            return False
        map_ = {}
        for i in s:
            map_[i] = map_.get(i, 0) + 1
        for j in t:
            if j not in map_ or map_[j] == 0:
                return False
            map_[j] = map_[j] - 1
        
        return True