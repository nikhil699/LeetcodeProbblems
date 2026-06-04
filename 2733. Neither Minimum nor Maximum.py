class Solution(object):
    def findNonMinOrMax(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 3:
            return -1
        
        firstThree = nums[:3]
        firstThree.sort()

        return firstThree[1]

        
sol = Solution()
nums = [3,2,1,4]
print(sol.findNonMinOrMax(nums))