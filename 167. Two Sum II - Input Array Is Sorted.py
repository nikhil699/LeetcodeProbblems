from collections import Counter
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        frequency = {}

        for index,item in enumerate(numbers):
            result = target - item
            if result in frequency:
                return [frequency[result], index+1]
            frequency[item] = index+1
        
        return []
        

sol = Solution()
numbers = [2,7,11,15]
target = 9
print(sol.twoSum(numbers,target))