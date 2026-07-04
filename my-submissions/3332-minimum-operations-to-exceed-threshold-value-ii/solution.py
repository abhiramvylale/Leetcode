class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)

        ans = 0
        
        def oper():
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, (x * 2 + y))

    
        for i in range(len(nums)):
            if nums[0] < k:
                oper()
                ans += 1
            else:
                break
        
        return ans
            


        
