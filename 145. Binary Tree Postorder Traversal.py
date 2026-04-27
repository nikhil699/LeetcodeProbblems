# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# postorder : left right root


class Solution(object):
    def postorderTraversal(self, root):

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        # result = []

        # def dfs(node):
        #     if node == None:
        #         return
            
        #     dfs(node.left)

        #     dfs(node.right)

        #     result.append(node.val) 

            
        
        # dfs(root)
        # return result


        # PostOrder -> left , right , root

        if root == None:
            return []
        
        stack01 = [root]
        stack02 = []
        result = []

        while stack01:
            node = stack01.pop()
            stack02.append(node)

            if node.left:
                stack01.append(node.left)
            
            if node.right:
                stack01.append(node.right)
        
        while stack02:
            result.append(stack02.pop().val)
        

        return result



        



root = [1,2,3,4,5,null,8,null,null,6,7,9]

sol =Solution()

print(sol.postorderTraversal(root))