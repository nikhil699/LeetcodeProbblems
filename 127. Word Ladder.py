from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        queue = deque()
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue.append((beginWord, 1))

        if beginWord in wordSet:
            wordSet.remove(beginWord)

        while queue: # 0(n)
            currentWord, steps = queue.popleft()

            if currentWord == endWord:
                return steps

            for item in range(len(currentWord)): # 0(m)
                wordChars = list(currentWord)
                originalCharacter = wordChars[item]

                for char in ("abcdefghijklmnopqrstuvwxyz"): # 0(26)
                    if originalCharacter == char:
                        continue
                    
                    wordChars[item] = char 
                    newWord = "".join(wordChars)

                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove((newWord))                
        
        return 0

        
sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol.ladderLength(beginWord, endWord, wordList))