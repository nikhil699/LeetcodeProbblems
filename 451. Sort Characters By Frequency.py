from collections import Counter
import heapq

class Solution(object):
    def frequencySort(self, s):

        """
        :type s: str
        :rtype: str
        """

        freq = Counter(s)
        heap = []
        result = []

        for item,value in freq.items():
            heapq.heappush(heap,(-value,item))

        while heap:
            item, value = heapq.heappop(heap)
            result.append(value * (-item))

        return "".join(result)

s = "tree"

sol = Solution()

print(sol.frequencySort(s))