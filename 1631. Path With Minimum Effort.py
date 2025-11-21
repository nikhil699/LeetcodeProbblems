import heapq

class Solution(object):
    def minimumEffortPath(self, heights):

        """
        :type heights: List[List[int]]
        :rtype: int
        """

        n = len(heights)
        m = len(heights[0])
        min_heap = []
        heapq.heappush(min_heap, (0,0,0)) # (current effort, row, col)
        directions = [(0,1),(-1,0),(1,0),(0,-1)]

        visited = set()

        while min_heap:
            effort, x, y = heapq.heappop(min_heap)

            if (x,y) in visited:
                continue
            visited.add((x,y))

            if x == n - 1 and y == m - 1:
                return effort

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if (nx,ny) not in visited and 0 <= nx < n and 0 <= ny < m:
                    newEffort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(min_heap, (newEffort, nx, ny))
            
        return -1



heights = [[1,2,2],[3,8,2],[5,3,5]]

sol = Solution()

print(sol.minimumEffortPath(heights))