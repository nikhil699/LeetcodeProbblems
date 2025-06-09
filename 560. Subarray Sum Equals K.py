# Prefix sum and Hashmap
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        maxSum = 0
        countFreq = {0:1} # define the base frequency for the subcount starts from 0 index having sum equals k




        for item in nums:
            maxSum += item

            if (maxSum - k) in countFreq:
                count += countFreq.get(maxSum - k)
            
            countFreq[maxSum] = countFreq.get(maxSum,0)+ 1
        
        return count

sol = Solution()

nums = [1,2,3]
k = 3

print(sol.subarraySum(nums,k))