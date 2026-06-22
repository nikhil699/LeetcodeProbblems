from collections import deque

class Solution(object):
    def findJudge(self, n, trust):

        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for u, v in trust:
            outdegree[u] += 1   # u trusts someone
            indegree[v] += 1    # v is trusted by someone


        for item in range(1, n + 1):
            if indegree[item] == n - 1 and outdegree[item] == 0:
                return item
        return -1

        # peopleList = defaultdict(list)

        # for to, fro in trust:
        #     peopleList[to].append(fro)

        # visited = set()
        # queue = deque()
        # visited.add(1)
        # queue.append(1)

        # while queue:
        #     item = queue.popleft()
            

        #     for element in peopleList[item]:
        #         if element not in visited:
        #             queue.append(element)
        #             visited.add(item)
               

        # for item in range(1,n + 1):
        #     if item not in visited:
        #         return item
        
        # return -1


sol = Solution()
n = 3
trust = [[1,3],[2,3],[3,1]]
print(sol.findJudge(n, trust))