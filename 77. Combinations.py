# Final Time Complexity
# O(C(n,k)⋅k)

# ​We generate C(n, k) combinations.
# For each valid combination, we copy a list of size k → O(k) work.
# So total time = number of combinations × time per combination.

# Final Space Complexity
# O(C(n,k)⋅k)+O(k)

# O(C(n, k) * k) → to store all combinations in the result.
# O(k) → maximum depth of the recursion stack.

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtracking(index, path):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(index, n + 1):
                path.append(i)
                backtracking(i + 1,path)
                path.pop()

        backtracking(1,[])
        return result

sol = Solution()
n = 4
k = 2
print(sol.combine(n,k))