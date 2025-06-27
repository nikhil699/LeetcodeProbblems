# Total complexity:
# ✅ O(E log N)
# Space: O(E + V)
# Overall: O(E + N)

# E → for the graph and heap

# N → if visited set is used to avoid unnecessary revisits
from collections import defaultdict
import heapq

class Solution(object):
    def findCheapestPrice(self,n, flights, src, dst, k):
    # Step 1: Build graph
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
    
    # Step 2: Priority queue: (total_cost, current_city, stops)
        heap = [(0, src, 0)]
    
    # visited dict to store best cost to a node with given stops
        visited = {}
    
        while heap:
            cost, city, stops = heapq.heappop(heap)
        
            if city == dst:
                return cost
        
            if stops > k:
                continue
        
            if (city, stops) in visited:
                continue
        
            visited[(city,stops)] = cost
        
            for neighbour, price in graph[city]:
                heapq.heappush(heap, (cost + price, neighbour, stops + 1))
                
    
        return -1

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

sol = Solution()
print(sol.findCheapestPrice(n,flights,src,dst,k))