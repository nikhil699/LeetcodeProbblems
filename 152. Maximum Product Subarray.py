class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_Sum = nums[0]
        max_Sum = nums[0]
        result = nums[0]

        for num in range(1,len(nums)):
            if nums[num] < 0:
                max_Sum, min_Sum = min_Sum, max_Sum

            max_Sum = max(nums[num] * max_Sum, nums[num])
            min_Sum = min(nums[num] * min_Sum, nums[num])

            result = max(max_Sum, result)
        
        return result




nums = [2,3,-2,4]

sol = Solution()

print(sol.maxProduct(nums))