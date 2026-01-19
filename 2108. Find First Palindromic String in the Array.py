class Solution(object):
    def firstPalindrome(self, words):

        """
        :type words: List[str]
        :rtype: str
        """

        def palindrome(word):
            left = 0
            right = len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        

        for item in words:
            if palindrome(item):
                return item
        
        return ""
    


sol = Solution()
words = ["abc","car","ada","racecar","cool"]
print(sol.firstPalindrome(words))