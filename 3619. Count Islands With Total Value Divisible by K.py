class Solution(object):
    def countIslands(self, grid, k):

        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """

        # using Graph

        n = len(grid) # rows
        m = len(grid[0]) # cols
        totalIslands = 0

        def dfs(i, j):
            if grid[i][j] == 0 and i < 0 and j < 0 and i > n and j > m:
                return

            directions = [(-1,0),(0,-1),(1,0),(0,1)]

            islandSum = grid[i][j]
            grid[i][j] = 0

            for direct in directions:
                x1 = i + direct[0]
                y1 = j + direct[1]

                if x1 >= 0 and y1 >= 0 and x1 < n and y1 < m and grid[x1][y1] != 0:
                    islandSum += dfs(x1, y1)
            
            return islandSum



        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] != 0:
                    islandSum = dfs(i, j)
                    if islandSum % k == 0:
                        totalIslands += 1
        

        return totalIslands



sol = Solution()

grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]
k = 5
print(sol.countIslands(grid, k))