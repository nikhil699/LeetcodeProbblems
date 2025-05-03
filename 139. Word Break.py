# Hint to Implement:
# Use a boolean DP array (dp[]) of size len(s) + 1.

# Iterate over all substrings and check if they exist in the wordDict.

# If dp[j] is True, and s[j:i] is in the dictionary, then set dp[i] = True.

# Return dp[len(s)] as the answer.

# Time Complexity : 0(n*n)
# Space complexity : 0(n)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)  # Convert list to set for O(1) lookup
        
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1,len(s) + 1):
            for j in range(0,i):
                if dp[j] == True and s[j:i] in wordSet:
                    dp[i] = True
                    break
        print(dp)
        
        return dp[len(s)]

s = "applepenapple"
wordDict = ["apple","pen"]

sol = Solution()

print(sol.wordBreak(s,wordDict))