import heapq
class Solution:
   def minCost(self, arr):
    # code here
    # 5, = [4,5,6]
    # 9 = [9, 6]
    # 15
    #  = 15 + 14
    #  [4, 2 , 7 , 6 , 9] = [6,7,6,9] = 6
    #  [12,7,9] = 12
    #  [12,16] = 16
    #  28 + 16 + 12 + 6 = 62 = [2,3,4,6]
        heap = []
    
        for item in arr:
            heapq.heappush(heap, item)
        
    
        overallCost = 0
    
        while len(heap) > 1:
            
            firstElement = heapq.heappop(heap)
            secondElement = heapq.heappop(heap)
            
            cost = firstElement + secondElement
            
            overallCost += cost
            
            heapq.heappush(heap, cost)
    


    
        return overallCost
        
    
   
sol = Solution()

arr = [4, 3, 2, 6]

print(sol.minCost(arr))