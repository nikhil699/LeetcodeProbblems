class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        product = 1

        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -1 * n
        
        while n > 0:
            if n % 2 == 1:
                product = product * x
            
            x = x * x
            n = n // 2
        
        return product

x = 2.00000
n = 10
sol = Solution()

print(sol.myPow(x,n))