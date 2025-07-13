# Time & Space Complexity:
# Time: O(n)
# Space: O(n) (for LPS array)


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev = s[::-1]
        temp = s + "#" + rev  # avoid overlap
        lps = [0] * len(temp)
        
        # KMP LPS table build
        for i in range(1, len(temp)):
            j = lps[i-1]
            while j > 0 and temp[i] != temp[j]:
                j = lps[j-1]
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j
    
        # lps[-1] gives us length of longest palindromic prefix
        to_add = s[lps[-1]:] # bcd
        return to_add[::-1] + s # dcbabcd

        
        
sol = Solution()

s = "aacecaaa"
print(sol.shortestPalindrome(s))