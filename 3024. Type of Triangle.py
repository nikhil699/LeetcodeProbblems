class Solution(object):
    def triangleType(self, nums):

        """
        :type nums: List[int]
        :rtype: str
        """

        nums.sort()

        first = nums[0]
        second = nums[1]
        third = nums[2]

        if first + second <= third:
            return "none"

        if first == second == third:
            return "equilateral"
        elif first != second != third:
            return "scalene"
        else:
            return "isosceles"
        

sol = Solution()

nums = [3,4,5]

print(sol.triangleType(nums))