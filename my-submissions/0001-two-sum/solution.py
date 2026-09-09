class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for index, element in enumerate(nums):
            if target - element in res:
                return res[target - element] , index
            res[element] = index
