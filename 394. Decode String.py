# Sure Nikhil, here's a simple 4-line explanation of the intuition:

# We use a stack to keep track of the string and repeat count before every [.
# When we see a digit, we build the full number (for multi-digit values like 10, 100).
# When [ appears, we push the current string and number onto the stack and reset them.
# When ] appears, we pop from the stack, repeat the current string, and append it to the previous one.

# Yeh approach nested encoding ko bhi handle kar leta hai — isi liye stack ka use karte hain.

# stack = [("", 3), ("a", 2)]

# Time Complexity: O(n)

# Space Complexity: O(n)

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        current_String = ""
        current_num = 0
        stack = []

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            elif char == "[":
                stack.append((current_String, current_num))
                current_num = 0
                current_String = ""
            
            elif char == "]":
                prev_char,num = stack.pop()
                current_String = prev_char + current_String * num
            
            else:
                current_String = current_String + char
        
        return current_String


s = "3[a]2[bc]"

sol = Solution()

print(sol.decodeString(s))