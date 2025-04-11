# Final Space Complexity: O(1) (Constant space)
# Final Space Complexity: O(1) (Constant space)


# Row Index (i // 3):

# i = 0, 1, 2 → Box Row = 0

# i = 3, 4, 5 → Box Row = 1

# i = 6, 7, 8 → Box Row = 2

# 🔹 Column Index (j // 3):

# j = 0, 1, 2 → Box Col = 0

# j = 3, 4, 5 → Box Col = 1

# j = 6, 7, 8 → Box Col = 2

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                item = board[i][j]

                if item == ".":
                    continue

                if item in rows[i] or item in cols[j] or item in boxes[i//3][j//3]:
                    return False
                
                rows[i].add(item)
                cols[j].add(item)
                boxes[i//3][j//3].add(item)
        
        return True
    
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()

print(sol.isValidSudoku(board))