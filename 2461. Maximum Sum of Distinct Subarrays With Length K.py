# using two pointer + hashmap
class Solution(object):
    def maximumSubarraySum(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        freq = {}
        maxSum = 0
        left = 0
        result = 0

        for right in range(0,len(nums)):
            freq[nums[right]] = freq.get(nums[right],0) + 1 
            maxSum += nums[right] 
            
            while right - left + 1 > k:
                freq[nums[left]] -= 1 

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                maxSum -= nums[left]

                left += 1

            if len(freq) == k:
                result = max(result, maxSum)


        return result
        
nums = [1,5,4,2,9,9,9]
k = 3


sol = Solution()

print(sol.maximumSubarraySum(nums,k))