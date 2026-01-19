class Solution(object):
    def canAliceWin(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """
        singleDigit = 0
        DoubleDigit = 0

        for number in nums:
            if number >= 10:
                DoubleDigit += number
            else:
                singleDigit += number
        
        if DoubleDigit == singleDigit:
            return False
        else:
            return True


sol = Solution()

nums = [1,2,3,4,10]

print(sol.canAliceWin(nums))