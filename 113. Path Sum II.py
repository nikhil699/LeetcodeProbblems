# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        def binaryTreeNode(node, count, path):
            if node is None:
                return
            
            count += node.val
            path.append(node.val)

            if node.left is None and node.right is None:
                if count == targetSum:
                    result.append(path)
            else:
                binaryTreeNode(node.left, count, path[:])
                binaryTreeNode(node.right, count, path[:])
            
        binaryTreeNode(root, 0, [])
        return result
            


# Build the tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
target = 7

# Call the function
sol = Solution()
print(sol.pathSum(root, target)) 


            

            
