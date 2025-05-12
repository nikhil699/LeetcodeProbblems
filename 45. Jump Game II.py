# At index j, you can jump up to nums[j] steps.
# So the farthest you can go from j is j + nums[j].
# ✅ If j + nums[j] >= i, it means:
# We can reach index i from index j, so it's a valid jump.


# Time: O(n^2) — two nested loops
# Space: O(n) — dp array

class Solution(object):
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0  # Starting point

        for i in range(1, n):
            for j in range(0, i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        
        print(dp)
        
        return dp[n-1]


nums = [2,3,1,1,4]

sol = Solution()

print(sol.jump(nums))