class Solution(object):
    def subtractProductAndSum(self, n):

        """
        :type n: int
        :rtype: int
        """
        productOverall = 1
        sumOverall = 0

        while n > 0:
            K = n % 10
            productOverall *= K
            sumOverall += K
            n = n / 10
        
        return productOverall - sumOverall


sol = Solution()

n = 234

print(sol.subtractProductAndSum(n))