class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxPrice = 0

        for item in range(1, len(prices)): # [7,1,5,3,6,4] minPrice = 7 
            if prices[item] <= minPrice: # 1 >= 7 minPrice = 1
                minPrice = prices[item]
            
            maxPrice = max(maxPrice, prices[item] - minPrice) # max(0,-6) max(1 - 5)
        

        return maxPrice


sol = Solution()
nums = [7,1,5,3,6,4]
print(sol.maxProfit(nums))