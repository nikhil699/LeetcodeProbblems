# Space Complexity: O(n)
# Time Complexity: O(n²)

class Solution(object):
    def findCircleNum(self, isConnected):

        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        provinces = 0
        visited = set()

        def dfs(node, visited):
            for neighbour in range(len(isConnected)):
                if neighbour not in visited and isConnected[node][neighbour] == 1:
                    visited.add(neighbour)
                    dfs(neighbour, visited)
            
            return


        for node in range(len(isConnected)):
            if node not in visited:
                provinces += 1
                dfs(node, visited)
        return provinces
    


sol = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]

print(sol.findCircleNum(isConnected))
