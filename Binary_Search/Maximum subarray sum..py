class Solution(object):
    def maxSubArray(self, nums):
        minSum = nums[0]
        maxSum = nums[0]

        for item in range(1,len(nums)):
            minSum = max(nums[item], nums[item] + minSum)
            maxSum = max(maxSum, minSum)
        


        return maxSum


nums = [10, 6, -16, 3, 0, 10,9, -5] # output = 22

sol = Solution()

print(sol.maxSubArray(nums))