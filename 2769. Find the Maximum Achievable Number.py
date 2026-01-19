class Solution(object):
    def theMaximumAchievableX(self, num, t):

        """
        :type num: int
        :type t: int
        :rtype: int
        """

        return num + 2 * t


        

sol = Solution()
num = 4
t = 1
num02 = 3
t02 = 2
print(sol.theMaximumAchievableX(num, t))
print(sol.theMaximumAchievableX(num02, t02))