class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """

        def dfs(startIndex):
            if startIndex >= len(arr) or visited[startIndex] == True or startIndex < 0:
                return False

            if arr[startIndex] == 0:
                return True

            visited[startIndex] = True

            return dfs(startIndex + arr[startIndex]) or dfs(startIndex - arr[startIndex]) 
        

        visited = [False] * len(arr)

        return dfs(start)
        



sol = Solution()
arr = [4,2,3,0,3,1,2]
start = 5
print(sol.canReach(arr,start))