class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = []

        for i in range(1,n+1):
            if n % i == 0:
                result.append(i)

                
        
        if len(result) < k:
            return -1
        else:
            return result[k-1]
            
n = 12
k = 3

sol = Solution()

print(sol.kthFactor(n,k))