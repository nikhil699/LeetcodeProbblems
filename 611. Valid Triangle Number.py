class Solution(object):
    def triangleNumber(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        count = 0

        for item in range(len(nums) - 1 , 1, -1):
            left = 0
            right = item - 1

            while left < right:
                if nums[left] + nums[right] > nums[item]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        
        return count


nums = [4,2,3,4]

sol = Solution()
print(sol.triangleNumber(nums))