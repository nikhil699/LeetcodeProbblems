class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(temperatures)

        for temp in range(0,len(temperatures)):
            while stack and temperatures[temp] > temperatures[stack[-1]]:
                item = stack.pop()
                result[item] = temp - item
            stack.append(temp)
        
        return result

temperatures = [73,74,75,71,69,72,76,73]

sol = Solution()

print(sol.dailyTemperatures(temperatures))


