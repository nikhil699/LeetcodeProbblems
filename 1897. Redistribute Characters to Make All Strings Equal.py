# Time : 0 ( n * k)
# Space : 0(1) max, 26 character will be there

from collections import defaultdict
class Solution(object):
    def makeEqual(self, words):

        """
        :type words: List[str]
        :rtype: bool
        """

        countFrequency = defaultdict(int)

        for item in words: # 0(n)
            for letters in item: # 0(k)
                countFrequency[letters] += 1
        
        for item in countFrequency:
            if countFrequency[item] % len(words) != 0:
                return False
        return True



words = ["abc","aabc","bc"]

sol = Solution()

print(sol.makeEqual(words))