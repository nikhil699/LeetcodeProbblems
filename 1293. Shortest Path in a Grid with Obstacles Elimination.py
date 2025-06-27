# Approach : first i have to put the initial node of the graph with steps and remaining steps as 0,1 and check their neighbour as having the path or not if not then i add that node in a queue and again check thier neighbour and also take +1 in steps while exporing any specific node neighbour and after explore all the whole node if i am getting the target node meand end then i return the number of steps otherwise return -1 

from collections import deque

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        if not grid:
            return []
        
        if k >= m + n - 2:
            return m + n - 2
        
        queue = deque()
        visited = set()

        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        queue.append((0,0,k,0)) # represent as starting node as 0,0 and k is the remaining steps, 0 is the steps which we take 

        visited.add((0,0,k))

        while queue:
            x, y, rem_steps, steps = queue.popleft()

            if x == m - 1 and y == n - 1:
                return steps
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    new_k = rem_steps - grid[nx][ny]

                    if new_k >= 0 and (nx,ny,new_k) not in visited:
                        queue.append((nx,ny,new_k,steps + 1))
                        visited.add((nx,ny,new_k))
        
        return -1


sol = Solution()
grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1

print(sol.shortestPath(grid,k))