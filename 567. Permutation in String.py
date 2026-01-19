from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):

        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        s1Length = len(s1)

        if len(s1) > len(s2):
            return False
        
        # countFreq = {}
        # s1CharacterCount = Counter(s1)

        left = 0


        # for right in range(len(s2)):
        #     countFreq[s2[right]] = countFreq.get(s2[right], 0) + 1

        #     if right >= s1Length:
        #         countFreq[s2[left]] -= 1

        #         if countFreq[s2[left]] == 0:
        #             del countFreq[s2[left]]
                
        #         left += 1
            
        #     if countFreq == s1CharacterCount:
        #         return True
        
        # return False

        charTableS1 = [0] * 26
        charTableS2 = [0] * 26

        for item in range(len(s1)):
            element = s1[item]
            charTableS1[ord(element) - ord('a')] += 1
        

        for item in range(len(s2)):
            element = s2[item]
            charTableS2[ord(element) - ord('a')] += 1

            if item >= s1Length:
                deleteItem = s2[left]
                charTableS2[ord(deleteItem) - ord('a')] -= 1
                left += 1
            

            if charTableS2 == charTableS1:
                return True
        
        return False

        
        

sol = Solution()

s1 = "ab"
s2 = "eidbaooo"

print(sol.checkInclusion(s1,s2))