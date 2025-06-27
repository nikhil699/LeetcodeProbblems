class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0 # total money in the bank
        week = 1         # starting amount for each Monday


        for day in range(1, n + 1):
            # Calculate the money to deposit for the current day
            # Each Monday (every 7 days), increase the "week" base
            total += week + (day - 1) % 7 
            if day % 7 ==0:
                week +=1

        return total


n = 4

sol = Solution()
print(sol.totalMoney(n))