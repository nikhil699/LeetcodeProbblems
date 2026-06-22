class Solution(object):
    def checkSubarraySum(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        remainderMap = {0:-1}
        remainder = 0
        prefixSum = 0


        for item in range(len(nums)):
            prefixSum += nums[item]
            remainder = prefixSum % k

            if remainder in remainderMap:
                if item - remainderMap[remainder] > 1:
                    return True
            
            else:
                remainderMap[remainder] = item

        return False

            
    


        

sol = Solution()
nums = [23,2,4,6,7]
k = 6
print(sol.checkSubarraySum(nums, k))