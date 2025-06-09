import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Min heap with (distance, point)
        heap = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (dist, [x, y]))
        
      
    
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
    


sol = Solution()

points = [[1,3],[-2,2]]
k = 1

print(sol.kClosest(points,k))