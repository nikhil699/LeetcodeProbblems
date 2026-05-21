# approact : first i have to put all the non overlapping interval on left hand side of new declared array result then check for the overlapping intervals then add all the remmaining intervals and return the array at the end.

class Solution(object):
    def insert(self, intervals, newInterval):

        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        # put all the non overlapping intervals on the left hand side
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # now i have to merged all the overlapping interval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])

            newInterval[1] = max(intervals[i][1], newInterval[1])

            i += 1
        
        result.append(newInterval)


        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        
        return result

              


sol = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]

print(sol.insert(intervals, newInterval))