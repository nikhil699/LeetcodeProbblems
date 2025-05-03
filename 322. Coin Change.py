# Tabulation
# Time Complexity: O(n * amount)
# Space Complexity: O(amount + 1) = O(amount)

# coin = 1:

# dp[1] = min(dp[1], dp[0]+1) → min(inf, 0+1) → dp[1] = 1

# dp[2] = min(dp[2], dp[1]+1) → min(inf, 1+1) → dp[2] = 2

# dp[3] = min(dp[3], dp[2]+1) → min(inf, 2+1) → dp[3] = 3

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


coins = [1,2,5]
amount = 11

sol = Solution()

print(sol.coinChange(coins,amount))
