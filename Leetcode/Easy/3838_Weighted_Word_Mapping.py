class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        string = "abcdefghijklmnopqrstuvwxyz"
        result = []
        for word in words:
            weight_sum = 0
            for char in word:
                i = string.find(char)
                weight_sum += weights[i]
            result.append(weight_sum % 26)
        answer = [string[-(i+1)] for i in result]
        return ''.join(answer)