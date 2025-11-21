class Solution:
    def longestSubarray(self, nums, k):
        maxLength = 0
        prefixSum = 0
        prefix = {0: -1}

        for item in range(len(nums)):
            prefixSum += nums[item]

            if (prefixSum - k) in prefix:
                maxLength = max(maxLength, item - prefix[prefixSum - k])
            else:
                prefix[prefixSum] = item
        
        return maxLength


nums = [1, 2, 3, -2, 5, 1]
k = 9
sol = Solution()
print(sol.longestSubarray(nums,k))
