class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(start,end):
            mid = (start + end ) // 2

            if start > end:
                return -1

            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                return binarySearch(mid + 1, end)
            else:
                return binarySearch(start, mid - 1)

        return binarySearch(0,len(nums) - 1)
            


sol = Solution()
nums = [-1,0,3,5,9,12]
numss = [5]
targett = 5
target = 9
print(sol.search(numss, targett))