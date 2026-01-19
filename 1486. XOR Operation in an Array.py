class Solution(object):
    def xorOperation(self, n, start):

        """
        :type n: int
        :type start: int
        :rtype: int
        """

        count_XOR = 0
        for item in range(n):
            count_XOR ^=  ( start + 2 * item )


        return count_XOR

n = 4
start = 3

sol = Solution()

print(sol.xorOperation(n,start))