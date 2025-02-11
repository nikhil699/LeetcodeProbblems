#  Worst Case: O(N*M) (due to BFS queue storage).
# Timecomplexity : 0(n*m)

from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = deque()
        n = len(mat)
        m = len(mat[0])

        for i in range(n): # length of rows
            for j in range(m): # length of columns
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        while queue:
            j,k = queue.popleft()
            for x1,y1 in directions:
                K1 = j + x1
                K2 = k + y1
                if 0 <= K1 < n and 0 <= K2 < m and mat[K1][K2] == -1:
                    mat[K1][K2] = mat[j][k] + 1
                    queue.append((K1,K2))

        return mat 
mat = [[0,0,0],[0,1,0],[0,0,0]]
sol = Solution()

print(sol.updateMatrix(mat))