class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def parity(item):
            if item % 2 == 0:
                return True
            else:
                return False

        for i in range(1,len(nums)):
            if parity(nums[i]) == parity(nums[i-1]):
                return False
        return True

        
sol = Solution()
nums = [2,1,4]

print(sol.isArraySpecial(nums))
