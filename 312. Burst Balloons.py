# Time Complexity : 0(n3)
# Space Complexity : 0(n2)
# dp[0][1] + dp[1][3] → means:

# Pehle tum left to k aur k to right ke andar ke balloons burst kar chuke ho, phir k ko last mein burst kar rahe ho.
# So it's like:
# “Assume every other balloon in that window is already burst except k. Now burst k and collect reward.”
# Length = 4
# 🔹 left = 0, right = 4 → k=1,2,3
# k=1: 138 + dp[0][1] + dp[1][4] = 24 + 0 + 120 = 144
# k=2: 118 + dp[0][2] + dp[2][4] = 8
# k=3: 158 + dp[0][3] + dp[3][4] = 40 + 15 = 55

class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]         # add 1 to both ends
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        # print(dp)

        # length = size of current window
        for length in range(2, n):      # length of window (at least 2)
            for left in range(0, n - length):  # starting index
                right = left + length          # ending index
                for k in range(left + 1, right):   # possible last balloon to burst
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                    )
        print(dp)

        return dp[0][n - 1]


nums = [3,1,5,8]

sol = Solution()
print(sol.maxCoins(nums))