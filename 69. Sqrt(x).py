class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0

        while i * i <= x:
            i += 1
        
        return i - 1

x = 8
sol = Solution()

print(sol.mySqrt(x))
       