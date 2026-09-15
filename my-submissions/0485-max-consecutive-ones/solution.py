class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if count > max_length:
                    max_length = count
                count = 0
            elif nums[i] == 1:
                count += 1
        if count > max_length:
            max_length = count
        return max_length

