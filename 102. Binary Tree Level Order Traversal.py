from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []

        if root is None:
            return []

        queue = deque()
        queue.append(root)

        while queue:
            output = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                output.append(node.val)
            
        
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(output)
        
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
print(sol.levelOrder(root)) 