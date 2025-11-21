from collections import Counter

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        # Frequency count of characters in substring
        freq = Counter(s)
        
        # Find first character with frequency < k
        for ch in freq:
            if freq[ch] < k:
                # split by this character and recursively solve
                parts = s.split(ch)
                ans = 0
                for part in parts:
                    ans = max(ans, self.longestSubstring(part, k))
                return ans
        
        # If all characters satisfy frequency >= k
        return len(s)


s = "aaabb"
k = 3


sol = Solution()

print(sol.longestSubstring(s,k))