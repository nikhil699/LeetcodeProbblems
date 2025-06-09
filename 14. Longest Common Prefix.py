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





Design Round question:

Design a ticket booking system for movies. For example: bookmyshow
Functionality to be implemented:
● Search movie(by name, by theatre name)
● Book ticket
● Cancel ticket
● List upcoming movies
I was told to write first human interfaces,not any language specific just human interface then I was told to 
design DB and freedom to choose any db, and then he found mistakes in each table.