# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import heapq
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        heap = []

        def inorder(root):
            if root is None:
                return 0
            
            inorder(root.left)
            heapq.heappush(heap, root.val)
            inorder(root.right)
        
        inorder(root)
        
        return heap[k - 1]
        


            

# Build the tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# Call the function
sol = Solution()
k = 1
print(sol.kthSmallest(root, k)) 