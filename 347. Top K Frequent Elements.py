from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)

        # Sort by (-freq, word)
        sorted_word = sorted(freq.keys(), key = lambda e : (-freq[e],e))
        
        return sorted_word[:k]

        

nums = [1,1,1,2,2,3]
k = 2

sol = Solution()

print(sol.topKFrequent(nums, k))