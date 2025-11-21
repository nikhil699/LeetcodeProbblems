class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()

        for right in range(0, len(s)):
            substring = s[right:right+10]

            if substring in seen:
                repeated.add(substring)
            else:
                seen.add(substring)
        
        return list(repeated)


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

sol = Solution()

print(sol.findRepeatedDnaSequences(s))