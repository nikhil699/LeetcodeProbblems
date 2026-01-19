class Solution(object):
    def minCostClimbingStairs(self, cost):

        """
        :type cost: List[int]
        :rtype: int
        """

        n = len(cost)

        DP = [0] * (n + 1)

        for item in range(2, n + 1):
            DP[item] = min(DP[item - 1] + cost[item - 1], DP[item - 2] + cost[item - 2])
        
        print(DP)
        return DP[-1]


cost = [10,15,20]
cost01 = [1,100,1,1,1,100,1,1,100,1]

sol = Solution()

print(sol.minCostClimbingStairs(cost))
print(sol.minCostClimbingStairs(cost01))