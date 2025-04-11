class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        frequency = {}

        for index,item in enumerate(nums):
            result = target - item

            if result in frequency:
                return [frequency[result],index]
            
            frequency[item] = index
            
            
        
        return []

nums = [2,7,11,15]
target = 9

sol = Solution()

print(sol.twoSum(nums,target))