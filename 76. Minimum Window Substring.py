# 76. Minimum Window Substring

# HashMap + Sliding Window
# Time Complexity: O(|s| + |t|)
# Space Complexity: O(|s| + |t|) (hashmaps store करेंगे frequency)
# Max Time 15 Min for Hard its 20 min.
# Problem Understanding : we have two strings and i have to return miimum window substrign jo ke second wali first mein ho complete
# s = "ADOBECODEBANC", t = "ABC" ismein t ko hame s mein dhudna hai sabse chote string jismein sare character aaa jaye
# Approach : Sliding Window and Hashmap
# step 01: 

from collections import Counter
class Solution(object):
    def minWindow(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: str
        """

        t_CharCount = Counter(t)
        s_CharCount = {}
        left = 0
        windowComplete = 0
        minLength = float('inf')
        minStr = ""

        for right in range(0, len(s)):
            s_CharCount[s[right]] = s_CharCount.get(s[right], 0) + 1

            if s[right] in t_CharCount and s_CharCount[s[right]] == t_CharCount[s[right]]:
                windowComplete += 1
            
            while windowComplete == len(t_CharCount):
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    minStr = s[left:right + 1]
                
                if s[left] in t_CharCount and s_CharCount[s[left]] <= t_CharCount[s[left]]:
                    windowComplete -= 1
                
                s_CharCount[s[left]] -= 1
                if s_CharCount[s[left]] == 0:
                    del s_CharCount[s[left]]
                
                left += 1
        
        return minStr
            


sol = Solution()

s1 = "ADOBECODEBANC"
t1 = "ABC"
s2 = "a"
t2 = "aa"
print(sol.minWindow(s1,t1))
print(sol.minWindow(s2,t2))