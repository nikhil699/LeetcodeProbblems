class Solution(object):
    def merge(self, intervals):

        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        mergeIntervals = [intervals[0]]
  
        for item in range(1, len(intervals)):
            prevInterval = mergeIntervals[-1]
            currInterval = intervals[item]

            if prevInterval[1] >= currInterval[0]:
                prevInterval[1] = max(prevInterval[1], currInterval[1])
            else:
                mergeIntervals.append(currInterval)
        
        return mergeIntervals


intervals = [[1,3],[2,6],[8,10],[15,18]]

sol = Solution()

print(sol.merge(intervals))