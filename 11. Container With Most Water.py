# using two pointers.
# store left array for all smaller element.
# store right array in a alarger element.

class Solution(object):
    def maxArea(self, height):

        """
        :type height: List[int]
        :rtype: int
        """

        # leftBucket = [0] * len(height)
        # rightBucket = [0] * len(height)
        # minHeights = height[0]
        # maxHeights = height[0]

        # for item in range(len(height)):
        #     minHeights = min(minHeights, height[item])
        #     leftBucket[item] = minHeights
        
        # print(leftBucket)

        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            heights = width * min(height[left], height[right])

            maxArea = max(maxArea, heights)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea





sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))