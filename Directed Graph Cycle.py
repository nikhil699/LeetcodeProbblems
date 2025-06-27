from collections import defaultdict
class Solution:
    def isCycle(self, V, edges):
        graph = defaultdict(list)
        visited = set()
        recStack = set()
        
        for u,v in edges:
            graph[u].append(v)
        
            
        def dfs(node):
            visited.add(node)
            recStack.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
                
                elif neighbour in recStack:
                    return True
            
            recStack.remove(node)
            return False
                    
                    
        for i in range(V):
            if i not in visited:
                if dfs(i):
                    return True
        return False

0-1,2
1-2
2-3