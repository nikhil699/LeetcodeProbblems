# Minimum Number Of Steps, Shortest Path : BFS.
# Path Explore : DFS.
# Time Complexity : 0(n * m)
# Space complexity is O(n * m) due to DFS recursion in the worst case, 
# Even if we modify the grid in-place, recursion stack space is still counted.
# Short answer: Haan. Chahe in-place ho, agar recursive DFS hai to space O(n × m) hi hoti hai.

class Solution(object):
    def numIslands(self, grid):

        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # using DFS

        rows = len(grid)
        cols = len(grid[0])
        numberOfIsland = 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != "1":
                return
            
            grid[i][j] = "0"
            direction = [(0,1),(-1,0),(0,-1),(1,0)]

            for direct in direction:
                x1 = i + direct[0]
                y1 = j + direct[1]

                if x1 >= 0 and y1 >= 0 and x1 < rows and y1 < cols and grid[x1][y1] == "1":
                    dfs(grid, x1, y1)

            return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    numberOfIsland += 1
        
        return numberOfIsland




grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
sol = Solution()

print(sol.numIslands(grid))
