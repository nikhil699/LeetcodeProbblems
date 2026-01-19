# Complexity	Value
# Time	O(m·n)
# Space	O(m + n)

class Solution(object):
    def setZeroes(self, matrix):
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        row = len(matrix)
        col = len(matrix[0])

        zero_rows = set()
        zero_cols = set()
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        

        for r in zero_rows:
            for i in range(col):
                matrix[r][i] = 0


        for c in zero_cols:
            for i in range(row):
                matrix[i][c] = 0
        

        return matrix


sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(sol.setZeroes(matrix))