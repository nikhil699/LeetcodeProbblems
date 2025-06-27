import heapq
# Time Compexity : 0(N*N log N)
# Space Complexity :  0(N * N)
class Solution(object):
    def swimInWater(self, grid):

        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        # time : 0(N * N)
        visited = [[False] * n for _ in range(n)]

        heap = []
        heap = [(grid[0][0], 0, 0)]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        while heap:
            time,src,target = heapq.heappop(heap)  #0(logn) for push and pop
            if src == n - 1 and target == n - 1:
                return time
            
            for x,y in directions:
                x1 = x + src
                y1 = y + target

                if 0 <= x1 < n and 0 <= y1 < n and not visited[x1][y1]:
                    heapq.heappush(heap, (max(time,grid[x1][y1]),x1,y1))
                    visited[x1][y1] = True
        
        return -1

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

sol = Solution()
print(sol.swimInWater(grid))