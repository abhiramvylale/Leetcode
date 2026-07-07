class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = {}
        for i in nums:
            if i not in ans:
                ans[i] = 1
            elif i in ans:
                ans[i] = ans[i] + 1

        return max(ans, key = ans.get)
