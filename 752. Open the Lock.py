from collections import deque

class Solution:
    def openLock(self, deadends, target):
        dead_state = set(deadends)
        visited = set()

        if "0000" in dead_state:
            return -1
        
        queue = deque()
        queue.append(("0000",0))

        visited.add("0000")

        while queue:
            # now we have current node and their count
            node,count = queue.popleft()

            if node == target:
                return count

            for i in range(4):
                digit = int(node[i])
                for index in [-1,1]:
                    newDigit = (digit + index) % 10
                    newCombo = node[:i] + str(newDigit) + node[i+1:]
                
                    if newCombo not in visited and newCombo not in dead_state:
                        visited.add(newCombo)
                        queue.append((newCombo, count + 1))
 
        return -1


deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

sol = Solution()

print(sol.openLock(deadends,target))
