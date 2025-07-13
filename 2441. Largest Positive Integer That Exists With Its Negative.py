class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_k = -1

        for num in nums:
            if -num in num_set and num > 0:
                max_k = max(max_k, num)

        return max_k


nums = [-1,10,6,7,-7,1]

sol = Solution()
print(sol.findMaxK(nums))