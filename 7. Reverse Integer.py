class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        k = 0
        sign = -1 if x < 0 else 1
        x = abs(x)


        while x != 0:
            p = x % 10
            k = k * 10 + p
            x = x // 10

        k = sign * k

        # Handle 32-bit integer overflow
        if k < -2**31 or k > 2**31 - 1:
            return 0
        
        return k

x = 123
x2 = -123

sol = Solution()

print(sol.reverse(x2))