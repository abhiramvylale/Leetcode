class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = []
        result = 0
        for i in nums:
            count = 0
            while i > 0:
                i = i // 10
                count += 1
            res.append(count)
        for i in res:
            if i % 2 == 0:
                result += 1
        return result
