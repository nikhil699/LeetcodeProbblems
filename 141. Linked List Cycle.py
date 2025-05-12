# Time complexity: 0(n)
# Space complexity : 0(1)

# Approach : Use two pointers:
# slow moves one step at a time
# fast moves two steps at a time
# If there's a cycle, fast will eventually meet slow (like two runners on a circular track).
# If there's no cycle, fast will reach the end (None).

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True


        return False 



head = [3,2,0,-4]
pos = 1

sol = Solution()

print(sol.hasCycle(head))