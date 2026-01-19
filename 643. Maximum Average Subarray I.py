class Solution(object):
    def findMaxAverage(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        maxAverage = 0
        left = 0
        maxSum = 0
        result = float('-inf')

        for i in range(0,len(nums)):
            maxSum += nums[i]

            if i >= k:
                maxSum -= nums[left]
                left += 1

            if i >= k - 1:
                result = max(result, maxSum / float(k))
        
        return result
            
            


sol = Solution()

nums = [1,12,-5,-6,50,3]
k = 4

print(sol.findMaxAverage(nums,k))