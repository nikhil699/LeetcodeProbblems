class Solution(object):
    def numSubarraysWithSum(self, nums, goal):

        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        prefixSum = 0
        prefix = {0:1}
        count = 0

        for item in range(len(nums)):
            prefixSum += nums[item]

            if (prefixSum - goal) in prefix:
                count += prefix[prefixSum - goal]
            
            prefix[prefixSum] = prefix.get(prefixSum, 0) + 1
        
        return count


nums = [0,0,0,0,0]
goal = 0

sol = Solution()

print(sol.numSubarraysWithSum(nums,goal))

