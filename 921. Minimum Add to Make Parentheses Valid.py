class Solution:
    def minimumAddToMakeValidParenthesis(self, nums):
        IP = 0
        OP = 0
        
        for item in nums:
            if item == "(":
                IP += 1
            else:
                if IP > 0:
                    IP -= 1
                else:
                    OP += 1
        
        return IP + OP



 
s = "()" # 0
s1 = "(((" # 3
s2 = "()))((" # 4
s4 = "())" # 1
sol = Solution()

print(sol.minimumAddToMakeValidParenthesis(s1))

print(sol.minimumAddToMakeValidParenthesis(s2))

print(sol.minimumAddToMakeValidParenthesis(s))

print(sol.minimumAddToMakeValidParenthesis(s4))