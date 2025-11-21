from collections import defaultdict, deque
from xml.etree.ElementTree import _Target

# 1. Convert the tree to an undirected graph
# Because in a tree, you can't go upward easily. So:
# For each node, store edges between node ↔ left and node ↔ right.
# 2. Do BFS from the target node
# Use a queue and track distance.
# When distance == K, collect all nodes at that level.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# Aspect	Complexity
# Time Complexity	O(n)
# Space Complexity	O(n)

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        graph = defaultdict(list)

        def buildGraph(node, parent):
            if node is None:
                return

            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            buildGraph(node.left, node)
            buildGraph(node.right, node)

        buildGraph(root, None)
        

        visited = set()
        queue = deque()
        visited.add(target.val)
        queue.append((target.val , 0)) # node and distance
        result = []

        while queue:
            node, distance = queue.popleft()
            if distance == k:
                result.append(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, distance + 1))
            
        return result
        

                


            
# Build the tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

_Target.val = 5
k = 2

sol = Solution()

print(sol.distanceK(root, _Target.val, k))