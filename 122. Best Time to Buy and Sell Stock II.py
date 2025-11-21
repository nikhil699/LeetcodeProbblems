class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0

        for item in range(1, len(prices)):
            if prices[item] >= prices[item - 1]:
                profit = profit + ( prices[item] - prices[item - 1] )
        
        return profit


sol = Solution()
nums = [7,1,5,3,6,4]

print(sol.maxProfit(nums))