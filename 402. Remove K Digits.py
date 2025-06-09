class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for item in num:
            while stack and k > 0 and stack[-1] > item:
                stack.pop()
                k -= 1
            stack.append(item)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        
        


        result = ''.join(stack).lstrip('0')

      

        return result if result else "0"


num = "1432219"
k = 3

sol = Solution()

print(sol.removeKdigits(num,k))