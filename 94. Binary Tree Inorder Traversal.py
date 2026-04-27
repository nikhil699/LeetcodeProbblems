# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# left root right


class Solution(object):
    # def inorderTraversal(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: List[int]
    #     """
    #     result = []
    #     def inorder(root):
    #         if root is None:
    #             return []
    #         inorder(root.left)
    #         result.append(root.val)
    #         inorder(root.right)
        
    #     inorder(root)
    #     return result
    

    def inorderTraversal(self, root):
        result = []
        stack = []
        curr = root

        # Jab tak current node hai ya stack khali nahi hota
        while curr or stack:
            # 1. Sabse pehle Left-most node tak jao aur raaste ke nodes stack mein dalo
            while curr:
                stack.append(curr)
                curr = curr.left
        
            # 2. Leftmost node ko pop karo aur result mein dalo (Ye Root wala part hai)
            curr = stack.pop()
            result.append(curr.val)
        
            # 3. Ab Right subtree check karne ke liye pointer move karo
            curr = curr.right
        
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
print(sol.inorderTraversal(root)) 