# Time Complexity : 0(n)
# Space Complexity : 0(n)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftSum = []
        left = 0

        rightSum = [0] * len(height)
        right = 0


        for i in range(len(height)):
            left = max(left, height[i])
            leftSum.append(left)

        for i in range(len(height)-1,-1,-1):
            right = max(right,height[i])
            rightSum[i] = right 
        
       

        result = 0

        for i in range(len(height)):
            result = result + (min(leftSum[i], rightSum[i]) - height[i])




        print(rightSum)
        print(leftSum)

        return result
        
sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(sol.trap(height))