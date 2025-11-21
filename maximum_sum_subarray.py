# Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.

# Examples:

# Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
# Output: 11
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

# Input: arr[] = {-2, -4}
# Output: -2
# Explanation: The subarray {-2} has the largest sum -2.

# Input: arr[] = {5, 4, 1, 7, 8}
# Output: 25
# Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.


class Solution:
    def maxSumSubarray(self, nums):
        total = nums[0]
        maxSum= nums[0]

        for item in range(1,len(nums)):
            total = max(nums[item], total + nums[item])
            maxSum = max(total,maxSum)

        return maxSum



nums01 = [2,3,-8,7,-1,2,3]
nums02 = [-4,-2]
nums03 = [5,4,1,7,8]

sol = Solution()

print(sol.maxSumSubarray(nums01))
print(sol.maxSumSubarray(nums02))
print(sol.maxSumSubarray(nums03))

