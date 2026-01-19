# Time: O(n²)
# Space: O(n²)
class Solution(object):
    def minInsertions(self, s):

        """
        :type s: str
        :rtype: int
        """

        # least common subsequence using DP

        n = len(s)
        rev = s[::-1]

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        item = dp[n][n]

        return n - item

        
s = "mbadm"

sol = Solution()

print(sol.minInsertions(s))