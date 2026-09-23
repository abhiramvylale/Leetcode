class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digit = 0
        for i in range(0, len(digits)):
            digit *= 10
            digit += digits[i]
        digit = digit + 1
        res = []
        while digit > 0:
            res.append(digit % 10)
            digit //= 10
        res = res[::-1]
        return res
