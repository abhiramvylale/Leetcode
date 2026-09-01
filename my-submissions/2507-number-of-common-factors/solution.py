class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = []
        n = min(a,b)
        for i in range(1, n+1):
            if a % i == 0 and b % i == 0:
                res.append(i)

        return len(res)
