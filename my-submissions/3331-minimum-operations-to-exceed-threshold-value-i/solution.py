class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        n = nums.copy()
        for i in nums:
            if i < k:
                n.remove(i)
                ans += 1
        return ans


