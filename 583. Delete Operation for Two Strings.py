class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        dp = [[0] * (m+1) for i in range(n+1)]
      

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        lis = dp[n][m]
       

        return m + n - 2 * lis

    

sol = Solution()

word1 = "sea"
word2 = "eat"

print(sol.minDistance(word1,word2))