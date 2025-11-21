# Time Complexity : 0(1) because we have to store 26 character only.
# Space Complexity : 0(n).

from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        maxFreq = 0
        maxLength = 0
        left = 0


        for right in range(0,len(s)): # 0(n)
            freq[s[right]] += 1 # 0(26)
            maxFreq = max(maxFreq, freq[s[right]])

            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        

        return maxLength
            



s = "ABACBBBCCC"
k = 2

sol = Solution()
print(sol.characterReplacement(s,k))