# Intuition

# Use a stack to track characters and their frequencies:
# Push each character along with its count.
# If the count of the top character becomes k, remove it (pop from stack).
# At the end, rebuild the string using the remaining characters and their counts.
# deeedbbcccbdaa

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []

        for item in s:
            if not stack or item != stack[-1][0]:
                stack.append([item,1])
            else:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()
        
        return ''.join(char * count for char, count in stack)



s = "pbbcggttciiippooaais"
k = 2

sol = Solution()

print(sol.removeDuplicates(s,k))