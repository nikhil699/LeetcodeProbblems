# Time : 0(n)
# Space : 0(26)
from collections import Counter
import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        



        # Step 1: Count frequency of each character
        freq = Counter(s)

        # Step 2: Max heap using negative frequencies
        max_heap = [(-count, char) for char, count in freq.items()]

      

        heapq.heapify(max_heap)
        

        result = []
        prev_count, prev_char = 0, ''

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)

        # If previous character still has remaining count, push it back
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

        # Update prev character to current one (with one less count)
            prev_count = count + 1
            prev_char = char
        

        output = ''.join(result)

        # Final check: if result is valid (length matches input)
        if len(output) != len(s):
            return ""
        return output


sol = Solution()

s = "aaab"
s1 = "aaabbacdd"
print(sol.reorganizeString(s1))