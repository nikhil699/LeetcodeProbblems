# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if inorder is None or postorder is None:
            return []
        
        self.inorder_index = {val: idx for idx, val in enumerate(inorder)}
        self.currPosition = len(postorder) - 1

        def buildTreefromPreorder(left,right):
            if left > right:
                return None
            
            currNode = postorder[self.currPosition] #3
            self.currPosition -= 1  # Move to next root for future calls

            # Create the tree node
            root = TreeNode(currNode)

            currIndex = self.inorder_index[currNode] #1
            # right comes before root node
            root.right = buildTreefromPreorder(currIndex + 1, right)
            root.left = buildTreefromPreorder(left, currIndex - 1)

            return root
        
        return buildTreefromPreorder(0,len(inorder) - 1)






# Build the tree manually
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)

# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)

# Call the function
sol = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(sol.buildTree(postorder, inorder)) 





        