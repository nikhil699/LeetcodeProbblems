# Time Complexity : 0(n) where n is the number of character in a given string.
# Space Complexity : 0(1) where n is the number of distinct character in a given word s/.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        freq = {}
        left = 0


        for item in range(0,len(s)):
            freq[s[item]] = freq.get(s[item], 0) + 1

            while freq[s[item]] > 1:
                freq[s[left]] -= 1
                left += 1
            
            maxLength = max(item - left + 1, maxLength)
        
        return maxLength

s = "abcabcbb"

sol = Solution()

print(sol.lengthOfLongestSubstring(s))