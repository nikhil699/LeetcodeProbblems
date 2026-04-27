import bisect

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        element = bisect.bisect_left(nums, target)

        return element


nums = [1,3,5,6]
target = 2

sol = Solution()

print(sol.searchInsert(nums, target))