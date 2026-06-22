class Solution(object):
    def largestOddNumber(self, num):

        """
        :type num: str
        :rtype: str
        """

        for item in range(len(num) - 1, -1, -1):
            if num[item] in {'1','3','5','7','9'}:
                return num[:item + 1]
            
        return ""   
        
sol = Solution()
num = "35427"

print(sol.largestOddNumber(num))