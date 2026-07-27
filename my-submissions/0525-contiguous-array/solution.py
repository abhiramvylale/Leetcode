class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict = {}
        dict[0] = -1
        ans = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in dict:
                ans = max(ans, i - dict[count])
            else:
                dict[count] = i
        
        return ans
