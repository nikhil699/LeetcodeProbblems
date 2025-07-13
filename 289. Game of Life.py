# Time Complexity : 0(m * n) where n ansd n is the number of rowa and columns
# Space complexity : 0(1) in pleace modification

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def countNeighbours(r,c):
            directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            cost = 0

            for x1,y1 in directions:
                xx = x1 + r
                yy = y1 + c
                if 0 <= xx < rows and 0 <= yy < cols and abs(board[xx][yy]) == 1:
                    cost += 1
            return cost
        
        for r in range(rows):
            for c in range(cols):
                live_neighbour = countNeighbours(r,c)

                if board[r][c] == 1 and (live_neighbour < 2 or live_neighbour > 3):
                    board[r][c] = -1 
                
                elif board[r][c] == 0 and live_neighbour == 3:
                    board[r][c] = 2
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
        
        return board
        

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

sol = Solution()

print(sol.gameOfLife(board))