class Solution(object):
    def productExceptSelf(self, nums):

        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        leftResult = 1
        rightResult = 1
        result = []

        for item in range(0,len(nums)):
            left_product[item] = leftResult
            leftResult = leftResult * nums[item]
        

        for item in range(len(nums) - 1, -1, -1):
            right_product[item] = rightResult
            rightResult = rightResult * nums[item]


        for item in range(len(nums)):
            element = left_product[item] * right_product[item]
            result.append(element)
        

        return result


sol = Solution()
nums = [1,2,3,4]

print(sol.productExceptSelf(nums))