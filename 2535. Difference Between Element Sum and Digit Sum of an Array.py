class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        target = sum(nums) # 25
        difference = 0
        P = 0

        for item in nums:
            if item >= 10:
                while item > 0:
                    K = item % 10
                    P = P + K
                    item = item / 10
                difference += P
                P = 0
            else:
                difference += item
        
        return target - difference


nums = [1,15,6,3]

sol = Solution()

print(sol.differenceOfSum(nums))