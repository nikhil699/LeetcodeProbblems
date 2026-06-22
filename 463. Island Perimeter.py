# Approach : Every land cell contributes 4 sides.
# Adjacent land cells share an edge, reducing the perimeter by 2.
# Traverse the grid once, add 4 for each land cell and subtract shared edges.

# Time Complexity: O(rows × cols)
# Space Complexity: O(1)

class Solution(object):
    def islandPerimeter(self, grid):

        """
        :type grid: List[List[int]]
        :rtype: int
        """

        parameter = 0

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1:
                    parameter += 4

                    if i > 0 and grid[i - 1][j] == 1:
                        parameter -= 2
                    
                    if j > 0 and grid[i][j - 1] == 1:
                        parameter -= 2
        
        return parameter


sol = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(sol.islandPerimeter(grid))