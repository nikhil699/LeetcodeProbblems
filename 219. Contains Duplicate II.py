class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_map = {}

        for index, num in enumerate(nums):
            if num in index_map and index - index_map[num] <= k:
                return True
            index_map[num] = index   # update last index
        return False
            


nums = [1,2,3,1]
k = 3

sol = Solution()

print(sol.containsNearbyDuplicate(nums,k))