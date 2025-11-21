# 1 Solution using heap 0(n log k)
# 2 Solution using deque(monotonic Queue).

import heapq
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Solution 01

        # heap = []
        # result = []

        # for item in range(0,k):
        #     heapq.heappush(heap,(-nums[item],item))
        
        # result.append(-heap[0][0])

        # for item in range(k, len(nums)):
        #     heapq.heappush(heap,(-nums[item],item))

        #     while heap and heap[0][1] <= item - k:
        #         heapq.heappop(heap)
            
        #     result.append(-heap[0][0])
        
        # return result

        # Solution 02

        result = []
        dq = deque()

        for item in range(len(nums)):
            
            # if index is out of window then pop from left
            while dq and dq[0] <= item - k:
                dq.popleft()


            # if item is less than the element at the top of queue then pop it 
            while dq and nums[dq[-1]] < nums[item]:
                dq.pop()


            # append index
            dq.append(item)


            if item >= k - 1:
                result.append(nums[dq[0]])
            

        return result


        


        
        
        
nums = [1,3,-1,-3,5,3,6,7]
k = 3

sol = Solution()
print(sol.maxSlidingWindow(nums, k))