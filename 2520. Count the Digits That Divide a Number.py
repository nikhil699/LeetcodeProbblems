class Solution(object):
    def countDigits(self, num):

        """
        :type num: int
        :rtype: int
        """

        count = 0
        newNumber = num

        while newNumber > 0:
            K = newNumber % 10
            if num % K == 0:
                count += 1
            newNumber = newNumber / 10
        
        return count



sol = Solution()

num = 121
num02 = 1239

print(sol.countDigits(num))
print(sol.countDigits(num02))