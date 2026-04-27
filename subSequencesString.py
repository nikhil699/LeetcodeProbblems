# Correct thinking kya honi chahiye
# Har word ke liye
# s word par pointer chalao
# word ke characters ko left → right match karo
# Agar pura word match ho gaya → valid subsequence

import bisect
from collections import defaultdict


class Solution(object):
    def subSequence(self, s, words):

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # Time Complexity : 0(W * S)
        # Space Complexity : 0(1)

        # totalSubsequenceWord = 0

        # for word in words: #0(n) where W is the length of words list.
        #     i = 0
        #     j = 0
        #     while i < len(s) and j < len(word): # 0(S) where m is the length of word given in s. 
        #         if s[i] == word[j]:
        #             j += 1
        #         i += 1
            
        #     if j ==len(word):
        #         totalSubsequenceWord += 1
                    
                

        # return totalSubsequenceWord
        
        # Now lets think of optimal part

        # kya hum s ko ek baar process karke reuse kar sakte hain?

        # Hum s ko preprocess karenge character → uske indices list

        # Step 1: Preprocess s word
        char_map = defaultdict(list)

        for i, ch in enumerate(s):
            char_map[ch].append(i)
        

        totalSubsequenceWord = 0

        # Step 2: Process each word
        for word in words:
            prev_index = -1
            found = True

            for ch in word:
                # agar char hi nahi hai s mein
                if ch not in char_map:
                    found = False
                    break
                
                index_list = char_map[ch] # [2, 7]

                # binary search: next index > prev_index
                pos = bisect.bisect_right(index_list, prev_index)

                if pos == len(index_list):
                    found = False
                    break

                prev_index = index_list[pos]

            if found:
                totalSubsequenceWord += 1

        return totalSubsequenceWord


s = "dsahjpjauf"
words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]

sol = Solution()

print(sol.subSequence(s,words))