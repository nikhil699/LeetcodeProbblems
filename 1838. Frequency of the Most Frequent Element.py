class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        prefix_sum = 0

        maxSum = 0

        for right in range(0,len(nums)):
            prefix_sum += nums[right]

            while nums[right] * (right - left + 1) - prefix_sum > k:
                prefix_sum -= nums[left]
                left += 1
            
            maxSum = max(maxSum , right - left + 1)
        
        return maxSum


nums = [1,4,8,13]
k = 5

sol = Solution()

print(sol.maxFrequency(nums,k))