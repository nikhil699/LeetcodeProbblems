class Solution(object):
    def climbStairs(self, n):


        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return n

        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for item in range(3, n + 1):
            dp[item] = dp[item - 1] + dp[item - 2]
        

        return dp[-1]

n1 = 2
n = 3

sol = Solution()

print(sol.climbStairs(n1))
print(sol.climbStairs(n))