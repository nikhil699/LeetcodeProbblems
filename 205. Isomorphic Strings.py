class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_s = []
        freq_t = []

        if len(s) != len(t):
            return False

        for item in s:
            freq_s.append(s.index(item))

        for item in t:
            freq_t.append(t.index(item))
        
        for item in range(0,len(s)):
            if freq_s[item] != freq_t[item]:
                return False
        
        return True

        
s = "paper"
t = "title"

sol = Solution()
print(sol.isIsomorphic(s,t))