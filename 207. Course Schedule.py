# defaultdict automatically creates a default value (like an empty list) for missing keys, so you don’t need to check or initialize them manually.

# With a normal dict, you’d need to write extra code like if key not in dict.
# Time: O(V + E), where V = numCourses and E = prerequisites

# Space: O(V + E) for graph + O(V) for visited

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # lets create a adjacency list
        graph = defaultdict(list)

        for keys,values in prerequisites:
            graph[values].append(keys)
        
        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            
            visited[node] = 1

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            visited[node] = 2
            return True 

        for node in range(0,numCourses):
            if dfs(node):
                return False
        return True
        
      







numCourses = 2, prerequisites = [[1,0]]

sol = Solution()

print(sol.canFinish(numCourses, prerequisites))