# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []
        def binaryTreeTraversal(node, pair):
            if node is None:
                return
            
            pair.append(str(node.val))
            
            if node.left is None and node.right is None:
                result.append("->".join(pair))
            
            else:
                # ek naye copy banata hai pair[:] har branch khud maintainance karte hai.
                binaryTreeTraversal(node.left, pair[:])
                binaryTreeTraversal(node.right, pair[:])
        
        binaryTreeTraversal(root, [])
        return result
            


# Build the tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# Call the function
sol = Solution()
print(sol.binaryTreePaths(root)) 
