# Problem Statement
# Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

#Input: s = "IceCreAm"
#Output: "AceCreIm"

class Solution:
    def stringLeftRight(self, input):

        vowels = set("aeiouAEIOU")
        s = list(input)
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1
        
        return "".join(s)


sol = Solution()
input = "IceCreAm"

print(sol.stringLeftRight(input))

