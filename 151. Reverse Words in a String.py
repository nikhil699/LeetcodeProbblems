class Solution(object):
    def reverseWords(self, s):
        # Split the string into words, removing extra spaces
        words = s.strip().split()
        # Reverse the list of words
        words.reverse()
        print(words)
        # Join the reversed words by a single space
        return ' '.join(words)


s = "the sky is blue"
sol = Solution()

print(sol.reverseWords(s))