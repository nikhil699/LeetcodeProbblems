class Solution(object):
    def judgeCircle(self, moves):

        """
        :type moves: str
        :rtype: bool
        """

        x = 0 # horizontal steps
        y = 0 # vertical steps
  

        for move in moves:
            if move == "U":
                x += 1
            elif move == "D":
                x -= 1
            elif move == "L":
                y -= 1
            else:
                y += 1
        
        if x == 0 and y == 0:
            return True
        else:
            return False


moves = "LL"
moves02 = "UD"

sol = Solution()

print(sol.judgeCircle(moves))
print(sol.judgeCircle(moves02))