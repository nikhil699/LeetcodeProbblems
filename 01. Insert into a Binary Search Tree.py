# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)
        
        elif val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        
        else:
            root.right = self.insertIntoBST(root.right,val)
        
        return root

sol = Solution()

root = [4,2,7,1,3]
val = 5

print(sol.insertIntoBST(root,val))