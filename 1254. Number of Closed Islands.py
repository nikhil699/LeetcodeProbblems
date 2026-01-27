class Solution(object):
    def closedIsland(self, grid):
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != 0:
                return
            grid[i][j] = 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # remove boundary connected lands
        for i in range(rows):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][cols-1] == 0:
                dfs(i, cols-1)

        for j in range(cols):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[rows-1][j] == 0:
                dfs(rows-1, j)

        # count closed islands
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1

        return count


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

sol = Solution()

print(sol.closedIsland(grid))