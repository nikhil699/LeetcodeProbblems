# Time:  O((E + N) log N) → which is typically referred as O(E log N).
# Each edge can be pushed into heap once.
# Heap push/pop is log N.
# Space: O(N + E).
# Graph takes O(E).
# Heap and visited take O(N).

import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        # Step 1: Build adjacency list
        graph = defaultdict(list)  # O(1) creation
        for u, v, w in times:      # O(E) where E = number of edges
            graph[u].append((v, w))  # O(1) per insertion

        visited = set()           # O(1)
        min_heap = [(0, k)]       # O(1) → heap initialized with (time, source)
        maxTime = 0               # O(1)

        # Step 2: Dijkstra's algorithm using min-heap
        while min_heap:                                # Runs O(N) times (each node at most once)
            time, node = heapq.heappop(min_heap)       # O(log N)

            if node in visited:                        # O(1)
                continue

            visited.add(node)                          # O(1)
            maxTime = max(maxTime, time)               # O(1)

            for neighbor, travelTime in graph[node]:   # O(degree of node)
                if neighbor not in visited:            # O(1)
                    heapq.heappush(min_heap, (time + travelTime, neighbor))  # O(log N)

        # Step 3: Final check
        return maxTime if len(visited) == n else -1    # O(1)


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

sol = Solution()

print(sol.networkDelayTime(times,n,k))