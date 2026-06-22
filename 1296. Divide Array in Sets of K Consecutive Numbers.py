# using hashmap
from collections import defaultdict

class Solution(object):
    def isPossibleDivide(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # 0(n2)
        map_frequency = defaultdict(int)

        for item in nums:
            map_frequency[item] += 1
        
        # while map_frequency:
        #     startPoint = min(map_frequency)

        #     for item in range(startPoint, startPoint + k):
        #         if item not in map_frequency:
        #             return False
                
        #         map_frequency[item] -= 1

        #         if map_frequency[item] == 0:
        #             del map_frequency[item]
        
        # return True

        # 0(n log n)

        nums.sort() # 0(n log n)

        for item in nums: #0(n)
            if map_frequency[item] > 0: #0(1)
                for i in range(item + 1, item + k):  #0(k) 
                    if map_frequency.get(i, 0) == 0: #0(1)
                        return False
                    map_frequency[i] -= 1 #0(1)
                map_frequency[item] -= 1 #0(1)
        return True



sol =  Solution()
nums = [1,2,3,3,4,4,5,6]
k = 4
print(sol.isPossibleDivide(nums, k))