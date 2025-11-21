# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        self.inorder_index = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def constructTree(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx] #3
            self.pre_idx += 1  

            root = TreeNode(root_val) #create node as root

            index = self.inorder_index[root_val] # Split inorder array into left and right parts 1
            root.left = constructTree(left, index - 1)
            root.right = constructTree(index + 1, right)

            return root
        
        return constructTree(0, len(inorder) - 1)





# Build the tree manually
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)

# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)

# Call the function
sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(sol.buildTree(preorder, inorder)) 