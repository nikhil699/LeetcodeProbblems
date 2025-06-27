# # Approach : i have to chcke and store the rotten oranges and fresh oranges and do BFS in all the node having 
# rotten oranges means having value as 2 and check thier neighbour and if find any fresh ornges is thier makes it as 
# rotten and store the count for doing this and at the end after all tranversal if any index having fresh oranges o 
# will return -1 otherwise return number of steps
# | Metric    | Complexity |
# | --------- | ---------- |
# | **Time**  | O(m × n)   |
# | **Space** | O(m × n)   |

from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])
        
        if rows == 1 and cols == 1 and grid[rows-1][cols-1] == 2:
            return 0
        
        queue = deque()
        countOranges = 0
        minutes = 0

        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    countOranges += 1
        

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
       
       

        while queue and countOranges > 0:
            for i in range(len(queue)):
                x,y = queue.popleft()
                for direct in directions:
                    x1 = x + direct[0]
                    y1 = y + direct[1]
                    
                    if 0 <= x1 < rows and 0 <= y1 < cols and grid[x1][y1] == 1:
                        countOranges -= 1
                        queue.append((x1,y1))
                        grid[x1][y1] = 2
                
            minutes += 1
        

        if countOranges > 0:
            return -1
        else:
            return minutes



grid = [[2,1,1],[0,1,1],[1,0,1]]
grid01 = [[2,1,1],[1,1,0],[0,1,1]]

sol = Solution()

print(sol.orangesRotting(grid01))