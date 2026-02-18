class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_decimal = int(a, 2)
        b_decimal = int(b, 2)

        result = a_decimal + b_decimal

        return bin(result)[2:]