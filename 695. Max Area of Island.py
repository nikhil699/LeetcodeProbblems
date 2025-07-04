class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row = len(grid)
        col = len(grid[0])
        sum = 0

        def dfs(grid,i,j,row,col):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != 1:
                return 0

            directions = [(0,1),(-1,0),(1,0),(0,-1)]
            grid[i][j] = 0
            sum = 1

            for direct in directions:
                x1,y1 = direct
                sum = sum + dfs(grid,i+x1,j+y1,row,col)
            
            return sum

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_sum = dfs(grid,i,j,row,col)
                    if max_sum >= sum:
                        sum = max_sum
        return sum


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

sol = Solution()

print(sol.maxAreaOfIsland(grid))