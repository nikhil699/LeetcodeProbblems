class Solution(object):
    def maxSubarraySumCircular(self, nums):

        total = sum(nums)
        # maxSubarray

        curMax = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            curMax = max(nums[i], curMax + nums[i])
            maxSum = max(maxSum, curMax)
        

        # circularMax

        curMin = nums[0]
        minSum = nums[0]

        for i in range(1, len(nums)):
            curMin = min(nums[i], curMin + nums[i])
            minSum = min(minSum, curMin)


        # If all numbers are negative:
        # total == minSum  means full array taken as min subarray
        if minSum == total:
            return maxSum

        # ---------- Final Answer ----------
        circularMax = total - minSum
        return max(maxSum, circularMax)
    


sol = Solution()
nums = [1,-2,3,-2]
print(sol.maxSubarraySumCircular(nums))