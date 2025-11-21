# Time Complexity : 0(n) where n is the number of character in a given string.
# Space Complexity : 0(1) where n is the number of distinct character in a given word s/.

def twDistinctCharacters(s):
    freq = {}
    maxSum = 0
    left = 0

    for right in range(0,len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > 2:
            freq[s[left]] -= 1


            if freq[s[left]] == 0:
                del freq[s[left]]

            left += 1
        
        maxSum = max(right - left + 1, maxSum)
    
    return maxSum

s = "ccaabbbacbdef"
print(twDistinctCharacters(s))