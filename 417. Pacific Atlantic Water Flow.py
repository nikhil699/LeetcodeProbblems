class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(heights) #rows
        cols = len(heights[0]) #cols
        
        if not heights:
            return []
        
        pacific_height = [[False] * cols for _ in range(rows)]
        atlantic_height = [[False] * cols for _ in range(rows)]

        def dfs(i, j, visited):
            visited[i][j] = True
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for dx, dy in directions:
                x1, y1 = i + dx, j + dy
                if 0 <= x1 < rows and 0 <= y1 < cols and not visited[x1][y1] and heights[x1][y1] >= heights[i][j]:
                    dfs(x1, y1, visited)
            

        for i in range(rows):
            dfs(i,0,pacific_height)
            dfs(i,cols-1,atlantic_height)
        
        for i in range(cols):
            dfs(0,i,pacific_height)
            dfs(rows-1,i,atlantic_height)
        
        result = []

        print(pacific_height)
        print(atlantic_height)

        for i in range(rows):
            for j in range(cols):
                if pacific_height[i][j] == True and atlantic_height[i][j] == True:
                    result.append([i,j])
        
        return result
        


sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(sol.pacificAtlantic(heights))
