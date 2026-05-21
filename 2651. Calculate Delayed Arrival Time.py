class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        
        overallTime = (arrivalTime + delayedTime) % 24

        

        if overallTime < 24:
            return overallTime
        else:
            return 0

        
sol = Solution()

arrivalTime = 15
delayedTime = 5

print(sol.findDelayedArrivalTime(arrivalTime, delayedTime))