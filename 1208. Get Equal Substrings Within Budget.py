class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        maxLength = 0
        left = 0
        absoluteSum = 0

        for right in range(0,len(s)):
            absoluteSum = absoluteSum + abs(ord(s[right]) - ord(t[right]))

            while absoluteSum > maxCost:
                absoluteSum -= abs(ord(s[left]) - ord(t[left]))

                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        

        return maxLength



s = "abcd"
t = "cdef"
maxCost = 3

sol = Solution()

print(sol.equalSubstring(s,t,maxCost))