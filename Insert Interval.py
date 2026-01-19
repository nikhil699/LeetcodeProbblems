class Solution(object):
    def insert(self, intervals, newInterval):

        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        intervals.append(newInterval)

        intervals.sort()
        result = [(intervals[0])]

        for item in range(1,len(intervals)):
            # prevInterval pointing to the same element in result top element
            prevInterval = result[-1]
            currInterval = intervals[item]

            if prevInterval[1] >= currInterval[0]:
                prevInterval[1] = max(prevInterval[1], currInterval[1])
            
            else:
                result.append(currInterval)

        return result        


sol = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]

print(sol.insert(intervals, newInterval))