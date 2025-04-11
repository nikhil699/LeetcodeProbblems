from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anangram_List = defaultdict(list)

        for item in strs:
            sortedWord = ''.join(sorted(item)) # because its return in a list of wordd and we want a string
            anangram_List[sortedWord].append(item)

        return anangram_List.values()
            
        
sol = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

print(sol.groupAnagrams(strs))