import heapq
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        # 2,2,3,5,6
        # 2,4,3,5,6
        # 4,4,3,5,6
        # 4,4,6,5,6
        # 8,4,6,5,6

        # using min heap 2,1,3,5,6 -> 

        min_heap = []

        for index, item in enumerate(nums):
            heapq.heappush(min_heap,(item, index))

        for item in range(k):
            item, index = heapq.heappop(min_heap)

            nums[index] *= multiplier

            heapq.heappush(min_heap, (nums[index], index))
        
        
        return nums


nums = [2,1,3,5,6]
k = 5
multiplier = 2


sol = Solution()

print(sol.getFinalState(nums, k, multiplier))