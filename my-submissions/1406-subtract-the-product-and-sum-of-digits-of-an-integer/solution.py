class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = n // 10
        product = 1
        sum = 0
        for i in digits:
            product *= i
            sum += i
        return (product - sum)
