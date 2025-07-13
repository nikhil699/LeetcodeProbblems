import math
class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prev = nums[-1]
        ops = 0

        for num in range(n-2,-1,-1):
            if nums[num] <= prev:
                prev = nums[num]
            else:
                parts = (nums[num] + prev - 1) // prev
                ops += parts - 1
                prev = nums[num] // parts
        
        return ops

s = Solution()
print(s.minimumReplacement([10, 7, 5, 18, 3]))