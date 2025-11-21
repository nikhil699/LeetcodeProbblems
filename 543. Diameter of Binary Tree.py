# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if i am standing at any node and i know the left height and right height then i will tell the diameter of that node as same i 
# will find for each node and update the max diameter from the specific node at last i will return that.

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Diameter at this node = left height + right height
            self.diameter = max(self.diameter, left + right)

            # return 1 + max(left, right)  # height of subtree

        dfs(root)
        return self.diameter

sol = Solution()

root = [1,2,3,4,5]

print(sol.diameter(root))