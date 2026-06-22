import heapq

class Solution(object):
    def findScore(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """

        indexFrequency = []
        markedArray = [False] * len(nums)
        score = 0

        for index, item in enumerate(nums): # [(1, 1), (2, 0), (2, 5), (4, 3), (5, 4), (3, 2)]
            heapq.heappush(indexFrequency,(item, index))
        
        while indexFrequency:
            value, idx = heapq.heappop(indexFrequency)

            if markedArray[idx] == True:
                continue
            
            score += value

            markedArray[idx] = True

            if 0 <= idx - 1 < len(nums):
                markedArray[idx - 1] = True
            if 0 <= idx + 1 < len(nums):
                markedArray[idx + 1] = True
        
        return score


sol = Solution()
nums = [2,1,3,4,5,2]
print(sol.findScore(nums))