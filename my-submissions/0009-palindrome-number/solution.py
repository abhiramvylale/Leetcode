class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        res = 0
        dum = x
        while dum > 0:
            res *= 10
            res += dum % 10
            dum //= 10
        
        if res == x:
            return True
        else:
            return False
            
