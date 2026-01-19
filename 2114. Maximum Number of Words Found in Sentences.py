class Solution(object):
    def mostWordsFound(self, sentences):

        """
        :type sentences: List[str]
        :rtype: int
        """

        maxWord = 0
        total = 0

        for item in sentences:
            total = len(item.split())
            maxWord = max(maxWord, total)
            total = 0
        

        return maxWord



sol = Solution()

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

print(sol.mostWordsFound(sentences))


