# Time Complexity: O(n * n)
# Because for each number of nodes i (from 2 to n), we try all possible roots (from 1 to i), resulting in two nested loops → O(n²).

# Space Complexity: O(n)

# Intuition (with Example for n = 3):
# We are trying every number from 1 to n as root, and for each root:

# Suppose we choose i as the root:
# Left Subtree will have nodes < i → so i-1 nodes.

# Right Subtree will have nodes > i → so n - i nodes.

# So, number of unique BSTs =
# (number of left subtrees) × (number of right subtrees)

# Which becomes:

# dp[i-1] * dp[n-i]


class Solution(object):
    def numTrees(self, n):
        # dp[i] will store number of unique BSTs for i nodes
        dp = [0] * (n + 1)
        
        # Base cases:
        dp[0] = 1  # Empty tree
        dp[1] = 1  # Single node tree

        # Fill dp[2] to dp[n]
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left = root - 1        # number of nodes in left subtree
                right = nodes - root   # number of nodes in right subtree
                dp[nodes] += dp[left] * dp[right]  # total trees with this root

        return dp[n]


n = 3

sol = Solution()

print(sol.numTrees(n))
