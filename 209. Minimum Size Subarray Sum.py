# It is a contigious subarray that means i will be using two pointers approach.

class Solution(object):
    def minSubArrayLen(self, target, nums):

        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        maxSubarraySize = float('inf')
        currSize = 0

        for right in range(len(nums)):
            currSize += nums[right]

            while currSize >= target:
                maxSubarraySize = min(maxSubarraySize, right - left + 1)
                currSize -= nums[left]
                left += 1

        if maxSubarraySize == float('inf'):
            return 0
        else:
            return maxSubarraySize
        

sol = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(sol.minSubArrayLen(target, nums))