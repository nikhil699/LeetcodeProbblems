class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        if not nums:
            return 0

        for item in range(1,len(nums)):
            if nums[item] != nums[left]:
                left += 1

                nums[left] = nums[item]
        
        return left + 1



nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()

print(sol.removeDuplicates(nums))