# Every node once → O(n)
# Every edge once (undirected means both directions are stored) → O(e)
# Time = O(n + e)

# graph (Adjacency List) → O(n + e)
# visited set → up to O(n)
# queue (for BFS) → up to O(n)
# # Time = O(n + e)



from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # lets make a adjacency list
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        component = 0

        for i in range(n):
            if i not in visited:
                component += 1
                queue = deque([i])

                while queue:
                    curr = queue.popleft()
                    for neighbour in graph[curr]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
        return component


