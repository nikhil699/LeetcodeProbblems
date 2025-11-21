class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        symbols = ["+","-","*","/"]
        stack = []

        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        
        return stack[-1]


# Tests
sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))         # 9
print(sol.evalRPN(["4","13","5","/","+"]))       # 6
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22