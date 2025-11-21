# Definition for a binary tree node.
# Time and Space Complexity.
# Time Complexity	O(n) – visit every node once
# Space Complexity	O(h) – recursion stack (h = height of tree)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.sum = 0

        def calculateSumOfTree(node):
            if node is None:
                return 0
            
            calculateSumOfTree(node.right)
            self.sum += node.val
            node.val = self.sum
            calculateSumOfTree(node.left)


        calculateSumOfTree(root)
        return root

             
# Build the tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)


sol = Solution()

print(sol.convertBST(root))       
