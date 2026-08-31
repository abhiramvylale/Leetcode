class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        n = num
        count = 0
        if num == 0:
            return True
        elif num % 10 == 0:
            return False
        else:
            return True
