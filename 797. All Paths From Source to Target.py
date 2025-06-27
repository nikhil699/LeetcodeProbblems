# n = number of nodes
# P = number of paths
# ⏱️ Time Complexity:
# we might visit every path from source to target
# Each path has max n nodes
# So: O(P * n)
# 🧠 Space Complexity:
# Stack depth = O(n) (DFS)
# Result = O(P * n) for storing paths


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # using DFS
        result = []
        target = len(graph) - 1

        def dfs(node,path):
            if node == target:
                result.append(list(path))
                return
            
            for neighbour in graph[node]:
                path.append(neighbour)
                dfs(neighbour,path)
                path.pop()

        dfs(0,[0])

        return result



graph = [[1,2],[3],[3],[]]

sol = Solution()

print(sol.allPathsSourceTarget(graph))