# Definition for a binary tree node.

# Iterative Approach

# if not root:
#             return []
        
#         result = []
#         stack = [root]

#         while stack:
#             node = stack.pop()

#             result.append(node.val)

#             if node.right:
#                 stack.append(node.right)
            
#             if node.left:
#                 stack.append(node.left)

        
#         return result


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def dfs(node):
            if node == None:
                return

            result.append(node.val)

            dfs(node.left)
            dfs(node.right)
            

        dfs(root)
        
        return result


root = [1,2,3,4,5,null,8,null,null,6,7,9]
sol = Solution()


print(sol.preorderTraversal(root))