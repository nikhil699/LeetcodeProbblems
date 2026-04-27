# Approach : Sab elements ko flatten karke sort karo
# Check karo ki sabka remainder (num % x) same hai, warna return -1
# Target = median element
# Har element ko median tak lane ke liye (abs(num - median) / x) operations count karo

class Solution(object):
    def minOperations(self, grid, x):

        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """

        result = []

        for item in grid:
            for element in item:
                result.append(element)
        
        rem = result[0] % x
        for item in result:
            if item % x != rem:
                return -1
        
        result.sort()

        medianNumber = result[ len(result) // 2 ]
        countOperation = 0

        for item in result:
            countOperation += abs(medianNumber - item) // x
        

        return countOperation


grid = [[1,5],[2,3]]
x = 1
sol = Solution()

print(sol.minOperations(grid, x))