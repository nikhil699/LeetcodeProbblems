# Time: O(N * M * 4^L)
# Where N x M is the size of the board and L is the length of the word.
# Space: O(L) where l is the length of word
# Due to recursion stack and marking visited in-place.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # through DFS

        n = len(board) # rows
        m = len(board[0]) # cols

        def dfs(x,y,index):
            if len(word) == index:
                return True
            
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != word[index]:
                return False

            temp = board[x][y]
            board[x][y] = "#"

            direction = [(-1,0),(0,1),(0,-1),(1,0)]

            for x1,y1 in direction:
                if dfs(x + x1, y + y1, index + 1):
                    return True
            
            board[x][y] = temp

            return False
            


        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False


sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(sol.exist(board,word))
