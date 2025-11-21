# Time Complexity:  O(n log n + k log n) = 0(k log n)
# Space Complexity: O(n)
# Compare first element (-freq)
# If equal → compare second element (word, lexicographically)

from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, words, k):

        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        count = Counter(words)
        result = []
        heap = []

        # Time Complexity:  O(n log n) log n for simgle push
        for item,freq in count.items():
            heapq.heappush(heap, (-freq,item))

        # Time Complexity:  O(k log n) log n for simgle pop
        for item in range(k):
            result.append(heapq.heappop(heap)[1]) 
        

        return result

        

words = ["i","love","leetcode","i","love","coding"]
k = 2

sol = Solution()

print(sol.topKFrequent(words, k))

        

            

       
        

        
    




        