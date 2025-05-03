# Definition for a binary tree node.
# Queue se har level ke nodes nikaalte hain

# Us level ke saare children queue mein daalte hain

# level_nodes mein values add karte hain

# left_to_right ke hisaab se usko reverse karte hain ya nahin

# result mein daalte hain

# Flag flip karte hain

# Time Complexity: O(n)
# Space Complexity: O(n)
# n = number of nodes in the binary tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        left_to_right = True
        result = []
        q = deque([root])

        while q:
            levelSize = len(q)
            levelWindow = []

            for i in range(0,levelSize):
                item = q.popleft() #1
                levelWindow.append(item.val)

                if item.left:
                    q.append(item.left)
                
                if item.right:
                    q.append(item.right)
            
            if left_to_right == False:
                levelWindow.reverse()
            
            result.append(levelWindow)

            left_to_right = not left_to_right
        
        return result



sol = Solution()

root = [3,9,20,0,0,15,7]

print(sol.zigzagLevelOrder(root))