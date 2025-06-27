import heapq

class Solution(object):
    def meetingRoomTwo(self, intervals):
        # Sort intervals by start time (returns a new sorted list)
        intervals.sort(key=lambda x: x[0])  # Do NOT assign this to intervals!

        heap = []
        for interval in intervals:
            start, end = interval
            # If a room is free (the earliest end time is <= start), reuse it
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            # Allocate the current meeting room (by end time)
            heapq.heappush(heap, end)

        return len(heap)

sol = Solution()
input = [[0,30],[5,10],[15,20]]
print(sol.meetingRoomTwo(input))  # Output should be2
