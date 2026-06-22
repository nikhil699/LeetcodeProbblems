class Solution(object):
    def partitionString(self, s):

        """
        :type s: str
        :rtype: int
        """

        countCharacters = set()
        count = 1

        for item in s:
            if item in countCharacters:
                count += 1
                countCharacters = set(item)
            else:
                countCharacters.add(item)
        
        return count





sol = Solution()
s = "abacaba"
print(sol.partitionString(s))