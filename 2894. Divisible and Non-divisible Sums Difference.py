class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """

        sumDivisibleByN = 0
        sumNotDivisibleByN = 0

        for item in range(1, n + 1):
            if item % m == 0:
                sumDivisibleByN += item
            else:
                sumNotDivisibleByN += item
        
        return sumNotDivisibleByN - sumDivisibleByN


sol = Solution()

n = 10
m = 3

print(sol.differenceOfSums(n, m))