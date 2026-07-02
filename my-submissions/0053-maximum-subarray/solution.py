class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = -100000000
        current = 0

        for i in nums:
            current = current + i

            if current > max:
                max = current

            if current < 0:
                current = 0

        return max
                
        
