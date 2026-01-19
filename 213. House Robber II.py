class Solution(object):
    def rob(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        
        if not nums:
            return 0

        def robber(arr):
            dp = [0] * len(arr)

            if len(arr) == 1:
                return arr[0]
        
            if not arr:
                return 0

            dp[0] = arr[0]

            dp[1] = max(arr[0], arr[1])

            for item in range(2, len(arr)):
                dp[item] = max(dp[item - 1], arr[item] + dp[item - 2])
            

            return dp[-1]
        
        # 1 to last element
        p = robber(nums[1:])
        # 0 to before last element
        k = robber(nums[:-1])
        

        return max(k, p)



nums = [2,3,2]
sol = Solution()

print(sol.rob(nums))