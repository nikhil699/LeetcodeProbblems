from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):

        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        visitedRooms = set()
        visitedRooms.add(0)
        queue = deque([0])

        while queue:
            item = queue.popleft()
            for key in rooms[item]:
                if key not in visitedRooms:
                    visitedRooms.add(key)
                    queue.append(key)
        

        if len(visitedRooms) == len(rooms):
            return True
        else:
            return False


sol = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms))