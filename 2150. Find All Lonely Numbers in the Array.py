from collections import defaultdict

class Solution(object):
    def findLonely(self, nums):

        """
        :type nums: List[int]
        :rtype: List[int]
        """

        lonelyNumber = defaultdict(int)

        for item in nums:
            lonelyNumber[item] += 1

        result = []

        for item in nums:
            preNumber = item - 1
            postNumber = item + 1

            if lonelyNumber[item] == 1 and preNumber not in lonelyNumber and postNumber not in lonelyNumber:
                result.append(item)
        
        return result



sol= Solution()
nums = [10,6,5,8]
print(sol.findLonely(nums))