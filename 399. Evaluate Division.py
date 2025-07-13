# O(N + Q × (V + E))
# Final Space Complexity:
# 𝑂(𝑉+𝐸+𝑄)
# V = unique variables (nodes)
# E = total edges (at most 2 per equation)
# Q = number of queries

from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)

        # Build graph
        # O(N)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))
        

        # O(V + E)
        def dfs(curr, target, visited):
            if curr == target:
                return 1.0
            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1:
                        return res * weight

            return -1.0

        # O(Q)
        results = []
        for num, den in queries:
            if num not in graph or den not in graph:
                results.append(-1.0)
            elif num == den:
                results.append(1.0)
            else:
                visited = set()
                results.append(dfs(num, den, visited))
        
        return results


sol = Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(sol.calcEquation(equations, values, queries))