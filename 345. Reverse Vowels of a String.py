class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1
        vowels = set('aeiouAEIOU')
        s = list(s) 

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        
        return "".join(s)


s = "leetcode"
sol = Solution()

print(sol.reverseVowels(s))