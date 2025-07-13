# Assign it immediately if any room is free.
# If no room is free, wait until the earliest room becomes free and then run the meeting there.
# Keep count of how many meetings happen in each room.
# In the end, return the room number which had the maximum number of meetings.

# Time:
# Sorting meetings: O(m log m)
# For m meetings: each heap op is O(log n) → O(m log n)
# Final = O(m log m + m log n)

# Space: O(n + m)
# (room counters + heaps)

class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        import heapq


        meetings.sort()  # sort by start time

        available = list(range(n))  # all rooms available initially
        heapq.heapify(available)

        busy = []  # (endTime, roomNumber)
        count = [0] * n  # meeting count for each room

        for start, end in meetings:
            # Free up rooms that are done before current meeting
            while busy and busy[0][0] <= start:
                endTime, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                endTime, room = heapq.heappop(busy)
                # Delay current meeting
                duration = end - start
                heapq.heappush(busy, (endTime + duration, room))

            count[room] += 1

        # Return room with max count (min index in case of tie)
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i


n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]

sol = Solution()

print(sol.mostBooked(n,meetings))