# Time: O(n log n) (due to sorting + binary search in loop)
# Space: O(1) (excluding sorting)

import bisect

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        count = 0
        nums.sort()

        for i in range(len(nums)):
            # for j in range(i+1,len(nums)):
            #     target = nums[i]+nums[j]
            #     if target >= lower and target <= upper:
            #         count += 1
            left = bisect.bisect_left(nums, lower - nums[i], i + 1)
            right = bisect.bisect_right(nums, upper - nums[i], i + 1)

            count += right - left

        
        return count
        
nums = [0,1,7,4,4,5]
lower = 3
upper = 6

sol = Solution()
print(sol.countFairPairs(nums, lower, upper))