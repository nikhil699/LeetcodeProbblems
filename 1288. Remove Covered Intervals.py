class Solution(object):
    def removeCoveredIntervals(self, intervals):

        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key=lambda x: (x[0], -x[1])) 
        coveredInterval = 0
        previousInterval = 0

        for start, end in intervals:
            if end > previousInterval:
                coveredInterval += 1
                previousInterval = end
        

        
        return coveredInterval # [[1,4],[2,8],[3,6]]


intervals = [[1,4],[3,6],[2,8]]

sol = Solution()

print(sol.removeCoveredIntervals(intervals))