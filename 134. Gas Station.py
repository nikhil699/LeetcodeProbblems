class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        index = 0
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        for item in range(0,len(gas)):
            total = total + gas[item] - cost[item]
            if total < 0:
                total = 0
                index = item + 1
        
        

        if total_gas < total_cost:
            return -1
        else:
            return index
        
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

sol = Solution()

print(sol.canCompleteCircuit(gas,cost))