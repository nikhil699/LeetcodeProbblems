# This is a classic backtracking problem.

class Solution(object):

    def letterCombinations(self, digits):

        """
        :type digits: str
        :rtype: List[str]
        """

        result = []

        phoneMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backtracking(index, currString):
            if len(digits) == len(currString):
                result.append(currString)
                return

            currDigit = digits[index]
            letters = phoneMap[currDigit]

            for character in letters:
                backtracking(index + 1, currString + character)

        backtracking(0, "")

        return result

        
        
sol = Solution()
digits = "23"
print(sol.letterCombinations(digits))