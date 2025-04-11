class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        result = []

        strs.sort()

        first = strs[0]
        last = strs[-1]

        for item in range(min(len(first),len(last))):
            if first[item] == last[item]:
                result.append(first[item])
            else:
                break
        
        return "".join(result)

sol = Solution()

strs = ["flower","flow","flight"]

print(sol.longestCommonPrefix(strs))