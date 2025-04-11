class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxCount = 0
        left = 0

        for right in range(0,len(nums)):
            if nums[right] == 0:
                count += 1
            
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            

            maxCount = max(maxCount, right - left)

        return maxCount

sol = Solution()

nums = [0,1,1,1,0,1,1,0,1]

print(sol.longestSubarray(nums))