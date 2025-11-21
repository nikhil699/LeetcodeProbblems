# Problem Statement:
# Given a string s, find the length of the longest substring that contains exactly two distinct characters.
# s = "ccaabbbacbdef"

class Solution:
    def twoDistinctCharacter(self,s):
        pair = {}
        left = 0
        count = 0

        for right in range(0,len(s)):
            pair[s[right]] = pair.get(s[right],0) + 1

            while len(pair) > 2:
                pair[s[left]] -= 1

                if pair[s[left]] == 0:
                    del pair[s[left]]
                
                left += 1
            
            count = max(count, right - left + 1)
        
        return count




sol = Solution()
s = "ccaabbbacbdef"
print(sol.twoDistinctCharacter(s))