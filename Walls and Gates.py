# Using BFS
# "Yes, the same approach will work. Since we need the shortest distance from 
# every empty land to the nearest hospital, I would treat all hospitals as starting points, put all of them 
# into the queue initially, and perform a multi-source BFS. Whenever I reach an unvisited empty land (INF), I update its 
# distance and push it into the queue."

from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        queue = deque()

        row = len(rooms)
        col = len(rooms[0])

        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while queue:
            src, dest = queue.popleft()

            for direct in direction:
                x1 = src + direct[0]
                y1 = dest + direct[1]

                if 0 <= x1 < row and 0 <= y1 < col and rooms[x1][y1] == 2147483647:
                    rooms[x1][y1] = rooms[src][dest] + 1
                    queue.append((x1,y1))
        
        return rooms


sol = Solution()

rooms = [
    [2147483647, -1,          0,          2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1,          2147483647, -1],
    [0,          -1,          2147483647, 2147483647]
]

print(sol.wallsAndGates(rooms))