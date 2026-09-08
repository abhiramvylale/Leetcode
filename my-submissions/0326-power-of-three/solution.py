class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 3 == 1 or n % 3 == 2:
            return False
        while n > 3:
            n = n / 3
        if n == 3:
            return True
        else:
            return False
