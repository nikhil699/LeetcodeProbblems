# Time complexity : O(n log k) for heap insertions where k is the number of destinations from the source and n is the all ickets + O(n) for DFS traversal where n is the number of ticket 
# overall = O(n log n)
# space complexity : 0(n) where n is the number of tickets given 
from collections import defaultdict
import heapq

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        graph = defaultdict(list)
        result = []
        
        # Build graph with min-heaps for lexicographical order
        # Each push into the min-heap (priority queue) takes O(log k) time where k is the number of destinations from that source.
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)

        # Recursively call DFS with backtrackking of storing the result 
        # we store at the end once the end is comming meand all nodes are finish then we do backtrack
        # We visit each ticket (edge) exactly once, and each DFS call pops one neighbor from the heap.

# So total DFS time = O(n)
        def dfs(airport):
            while graph[airport]:
                next_neighbour = heapq.heappop(graph[airport])
                dfs(next_neighbour)
            result.append(airport)

        
        dfs('JFK')

        return result[::-1]


sol = Solution()
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

print(sol.findItinerary(tickets))