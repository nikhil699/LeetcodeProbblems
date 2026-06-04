class Solution(object):
    def countSubarrays(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        maxCount = 0

        for item in range(len(nums) - 2):
            if 2 * (nums[item] + nums[item + 2]) == nums[item + 1]:
                maxCount += 1
        

        return maxCount


sol = Solution()
nums = [1,2,1,4,1]
print(sol.countSubarrays(nums))