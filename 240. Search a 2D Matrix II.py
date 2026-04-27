class Solution(object):
    def searchMatrix(self, matrix, target):

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = 0
        cols = len(matrix[0]) - 1

        while rows < len(matrix) and cols >= 0:
            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] > target:
                cols -= 1
            else:
                rows += 1
        
        return False




matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]
target = 5

sol = Solution()

print(sol.searchMatrix(matrix,target))