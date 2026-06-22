class Solution(object):
    def findRectangleGraph(self, board):
        
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 0:
                    height = 0
                    width = 0
                    curr = c
                    # width
                    while curr < cols and board[r][curr] == 0:
                        width += 1
                        curr += 1
                    
                    curr = r
                    # height
                    while curr < rows and board[curr][c] == 0:
                        height += 1
                        curr += 1

                    return (r, c, width, height)


sol = Solution()

image1 = [
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1],
[1, 1, 1, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1],
]

print(sol.findRectangleGraph(image1))
