# Approach : My approach for this problem is to initialize two variables: currSum and maxSum. and then i iterate the entire array, and for each element, I add it to currSum. At each step, I compare the current sum (currSum) with the value of the current element and assign the greater value to currSum. This means if the current sum becomes negative, we start a new subarray from the current element. Finally, I update maxSum with the larger value between maxSum and currSum, and return maxSum at the end.

# Timne Complexity : 0(n) where n is the number of elelment in the given array nums

# Space Complexity : 0(1)


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = nums[0]
        maxSum = nums[0]

      

        for i in range(1,len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum,currSum)

        return maxSum
                
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()

print(sol.maxSubArray(nums))