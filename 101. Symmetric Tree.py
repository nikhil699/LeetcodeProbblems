# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):

        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def mirror(left, right):
            if left is None and right is None:
                return True

            if right is None or left is None:
                return False
        
            if left.val != right.val:
                return False

            return mirror(left.left, right.right) and mirror(left.right, right.left)
            
            
        
        return mirror(root,root)
            
        


# Build the tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# Call the function
sol = Solution()
print(sol.isSymmetric(root)) 