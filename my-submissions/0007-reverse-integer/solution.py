class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        sign = 0
        
        if x > 0:
            sign = 1
        elif x < 0:
            sign = -1

        x *= sign

        while x != 0:
            res *= 10
            res += x % 10
            x //= 10

        res *= sign

        if res < (-2 ** 31) or res > ((2 ** 31) - 1):
            return 0
        else:
            return res

        

