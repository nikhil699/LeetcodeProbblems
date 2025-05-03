from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1

        if not grid:
            return -1
        
        if rows == 1 and cols == 1 and grid[0][0] == 0:
            return 1
        
        directions = [(0,1),(1,0),(-1,1),(1,-1),(0,-1),(-1,0),(1,1),(-1,-1)]

        queue = deque()
        queue.append((0,0,1)) 

        while queue:
            row,col, dist = queue.popleft()

            if row == rows - 1 and col == cols - 1:
                return dist
            
            for direct in directions:
                x1 = row + direct[0]
                y1 = col + direct[1]

                if 0 <= x1 < rows and 0 <= y1 < cols and grid[x1][y1] == 0:
                    queue.append((x1,y1,dist + 1))
                    grid[x1][y1] = 1
        
        return -1
                





grid = [[0,0,0],[1,1,0],[1,1,0]]

sol = Solution()

print(sol.shortestPathBinaryMatrix(grid))