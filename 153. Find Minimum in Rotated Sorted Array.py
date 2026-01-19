# using binary search
class Solution(object):
    def findMin(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]: # yes
                left = mid + 1
            else:                               # No
                right = mid
        
        return nums[right]
    


nums = [3,4,5,1,2]

sol = Solution()

print(sol.findMin(nums))