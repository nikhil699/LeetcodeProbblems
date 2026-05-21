class Solution(object):
    def isGood(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """

        countFrequency = {}

        for item in range(len(nums)):
            countFrequency[nums[item]] = countFrequency.get(nums[item], 0) + 1
        

        for item in range(1, len(nums)):
            if item not in countFrequency:
                return False
        


        if countFrequency.get(len(nums) - 1) >= 2:
            return True
        else:
            return False


nums = [1, 3, 3, 2]
    
sol = Solution()
print(sol.isGood(nums))