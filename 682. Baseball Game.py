# using Stack
class Solution(object):
    def calPoints(self, operations):

        """
        :type operations: List[str]
        :rtype: int
        """

        stack = []

        for item in operations:
            if item == "C":
                stack.pop()
            elif item == "D":
                stack.append(stack[-1] * 2)
            elif item == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(item)) 
        
        return sum(stack)
            
            

sol = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
print(sol.calPoints(ops))