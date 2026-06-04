# Problem Understanding : using BFS check karenge neighbour of 1 and count the distance from it and update the matrix once iterate the whole matrix then return at the end.
from collections import deque

class Solution(object):
    def updateMatrix(self, mat):

        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        queue = deque()
        rows = len(mat)
        cols = len(mat[0])
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while queue:
            x1, y1 = queue.popleft()

            for direct in directions:
                xx = x1 + direct[0]
                yy = y1 + direct[1]

                if 0 <= xx < rows and 0 <= yy < cols and mat[xx][yy] == -1:
                    mat[xx][yy] = mat[x1][y1] + 1
                    queue.append((xx,yy))
        

        return mat
    
mat = [[0,0,0],[0,1,0],[1,1,1]]

sol = Solution()

print(sol.updateMatrix(mat))