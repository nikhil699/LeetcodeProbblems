class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        result = [0] * n

        for i in range(n):
            result[i] = s[(i+k) % n]


        return ''.join(result)

s = "dart"
k = 3

sol = Solution()
print(sol.getEncryptedString(s,k))