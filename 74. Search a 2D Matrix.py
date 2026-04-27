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


sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix, target))