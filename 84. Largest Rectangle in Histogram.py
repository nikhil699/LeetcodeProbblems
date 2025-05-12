class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)

        # Step 1: Compute Previous Smaller Element (PSE)
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        


        # Step 2: Compute Next Smaller Element (NSE)
        right = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        


        # Step 3: Compute max area
        maxArea = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            maxArea = max(maxArea, area)

        return maxArea


sol = Solution()

heights = [2,1,5,6,2,3]

print(sol.largestRectangleArea(heights))