import heapq
from math import ceil
class Solution(object):
    def maxKelements(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        minHeap = []

        score = 0

        for item in nums:
            heapq.heappush(minHeap, -item) # (10,3,3,3,1)
        
        for item in range(k):
            item = heapq.heappop(minHeap)
            actualValue = item * (-1)
            score += actualValue
            newValue = (actualValue + 2) // 3
            heapq.heappush(minHeap, -newValue)
        
        return score
        


        

# Approach
# nums = [10,10,10,10,10]
# for item in range(len(nums)):, score = 0
# score += nums[item]
# nums[i] = ceil(nums[i] / 3)

sol = Solution()
nums = [10,10,10,10,10]
k = 5
print(sol.maxKelements(nums, k))
        