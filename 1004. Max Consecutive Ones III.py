class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        maxCount = 0
        count = 0

        for right in range(0, len(nums)):
            if nums[right] == 0:
                count += 1
            
            while count > k:
                if nums[left] == 0:
                    count -= 1
            
                left += 1
            
            maxCount = max(maxCount, right - left + 1)
        
        return maxCount

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2


sol = Solution()

print(sol.longestOnes(nums,k))

