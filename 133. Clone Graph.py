from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        visited = {}  # original node -> cloned node
        queue = deque([node])
        # {1:1}
        visited[node] = Node(node.val)
        


        while queue:
            # curr.val = 1
            # curr.neighbour = [2,4]
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in visited:
                # Clone and store the neighbor
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Append the cloned neighbor to the current cloned node's neighbors
                visited[curr].neighbors.append(visited[neighbor])

        return visited[node]


# Here are **comprehensive test cases** you can use to validate your `cloneGraph` function implementation. These cover edge cases, simple cases, and more complex graphs.

# ---

## 1. **Empty Graph**

# **Test:**
# ```python
node = None
result = Solution().cloneGraph(node)
print(result)  # Expected output: None
# ```

# ---

## 2. **Single Node, No Neighbors**

# **Test:**
# ```python
single = Node(1)
result = Solution().cloneGraph(single)
print(result.val)  # Expected output:1
print(result.neighbors)  # Expected output: []
# ```

# ---

##3. **Two Nodes, One Edge**

# **Test:**
# ```python
node1 = Node(1)
node2 = Node(2)
node1.neighbors = [node2]
node2.neighbors = [node1]
result = Solution().cloneGraph(node1)
print(result.val)  #1
print(result.neighbors[0].val)  #2
print(result.neighbors[0].neighbors[0].val)  #1
# ```

# ---

## 4 **Four Nodes, Cycle**

# Graph:
# ```
# 1 --2
# |    |
# 4 --3
# ```
# **Test:**
# ```python
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
result = Solution().cloneGraph(node1)
print(result.val)  # 1print(sorted([n.val for n in result.neighbors]))  # [2, 4]
# ```

# ---

##5. **Self-loop**

# **Test:**
# ```python
node1 = Node(1)
node1.neighbors = [node1]
result = Solution().cloneGraph(node1)
print(result.val)  # 1print(result.neighbors[0].val)  # 1print(result.neighbors[0] is result)  # True (should be True for the clone)
# ```

# ---

## 6 **Disconnected Graph (Only the connected component from the starting node is cloned)**

# If you want to test this, you can have:
# ```python
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2]
# node3 is disconnected
result = Solution().cloneGraph(node1)
print(result.val)  # 1
print([n.val for n in result.neighbors])  # [2]
# ```
# Node3 will not appear in the cloned graph since it's not reachable from node1.

# ---

# ## **Tips for Testing**
# - Always check that the cloned nodes are new objects (not the same as the originals):  
#   `assert result is not node1`
# - Check that neighbor links are preserved and deep-copied.

# ---

# **Let me know if you want helper functions for printing or verifying the graph structure!**