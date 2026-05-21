# Time Complexity:
# O(n log 10^7)
# Space:
# O(1)

from math import ceil

class Solution(object):
    def minSpeedOnTime(self, dist, hour):

        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        
        if hour <= len(dist) - 1:
            return -1

        def canReachOnTime(speed):

            result = 0

            for i in range(len(dist) - 1):
                result += ceil(dist[i] / float(speed))

            result += dist[-1] / float(speed)

            return result <= hour
        

        low = 1
        high = 10**7
        answer = -1

        while low <= high:
            mid = (low + high) // 2
            
            if canReachOnTime(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1 
        

        return answer

        


sol = Solution()

dist = [1,3,2]
hour = 6

print(sol.minSpeedOnTime(dist, hour))