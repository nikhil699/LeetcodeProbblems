# Time Complexity : 0(n*m)
# Space complexity : 0(n*m)


# text1 = "a b c d e"
# text2 = "a c e"

# Matrix size: 6 x 4 (including extra row/column for empty strings)



#    '' a c e
# '' 0  0 0 0
#  a 0  1 1 1
#  b 0  1 1 1
#  c 0  1 2 2
#  d 0  0 0 0
#  e 0  0 0 0



class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        # using DP

        n = len(text1)
        m = len(text2)

        dp = [[0]*(m+1) for _ in range(n+1)]



        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        #  print(dp)
        
        return dp[n][m]


text1 = "abcde"
text2 = "ace"

sol = Solution()

print(sol.longestCommonSubsequence(text1,text2))