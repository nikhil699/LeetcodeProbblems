# Prefix Sum + hashmap
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k <= 1: 
            return 0


        count = 0
        left = 0
        prod = 1

        for right in range(0,len(nums)):
            prod *= nums[right]

            while prod >= k:
                prod //= nums[left]
                left += 1

            # all subarrays ending at `right` with start >= left are valid
            count += right - left + 1 
         
        
        return count

            

nums = [10,5,2,6]
k = 100

sol= Solution()

print(sol.numSubarrayProductLessThanK(nums, k))