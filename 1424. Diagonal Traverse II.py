class Solution(object):
    def findDiagonalOrder(self, nums):

        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
        count_digonal = {}

        for i in range(0, len(nums)):
            for j in range(0, len(nums[i])):
                diagonal = i + j
                if diagonal not in count_digonal:
                    count_digonal[diagonal] = []
                count_digonal[diagonal].append(nums[i][j])
        
        
        result = []
        # reversed() O(1)
        for item in count_digonal:
            result.extend(reversed(count_digonal[item]))
        

        return result


sol = Solution()

nums = [[1,2,3],[4,5,6],[7,8,9]]

print(sol.findDiagonalOrder(nums))