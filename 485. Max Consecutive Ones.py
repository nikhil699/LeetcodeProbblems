class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxCounted = 0
        
        for item in nums:
            if item == 1:
                count += 1
            else:
                count = 0
            maxCounted = max(maxCounted, count)
        
        return maxCounted


sol = Solution()
nums = [1,1,0,1,1,1]

print(sol.findMaxConsecutiveOnes(nums))