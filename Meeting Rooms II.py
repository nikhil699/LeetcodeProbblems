"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        minHeap = []

        intervals.sort(key=lambda x:x[0])
        
        for interval in intervals:
            if minHeap and minHeap[0] <= interval[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap,interval[1])
    
        return len(minHeap)

            

intervals = [(0,40),(5,10),(15,20)]

sol = Solution()

print(sol.minMeetingRooms(intervals))