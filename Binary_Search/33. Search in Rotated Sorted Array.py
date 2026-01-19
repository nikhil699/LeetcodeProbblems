class Solution(object):
    def search(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1

        
        if nums[0] == target:
            return 0

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[left] <= nums[mid]:  # Left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else: # Right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        
        return -1
        

nums = [4,5,6,7,0,1,2]
target = 0



sol = Solution()

print(sol.search(nums,target))