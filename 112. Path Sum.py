# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
        def binaryTreeSumPath(node, overallSum):
            if node is None:
                return False
            
            overallSum += node.val
            
            if node.left is None and node.right is None:
                return overallSum == targetSum
            
                       
            return ( binaryTreeSumPath(node.left, overallSum)
            or binaryTreeSumPath(node.right, overallSum) )
        
        return binaryTreeSumPath(root, 0)
    

# Build the tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# Call the function
sol = Solution()
target = 32
print(sol.hasPathSum(root, target)) 