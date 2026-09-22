class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        res = 0
        for i in d:
            if d[i] == 1:
                res += i
        return res
