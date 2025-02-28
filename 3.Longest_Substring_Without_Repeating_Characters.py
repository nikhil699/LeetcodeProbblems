# While loop (left pointer moves forward when duplicate found) → O(N) overall
# Har character at most ek baar remove hota hai, toh left pointer bhi max N times move karega.
# 🔹 Total Time Complexity: O(2N) ≈ O(N)

# Dono pointers (left and right) worst case mein N steps chalenge, toh overall linear time complexity (O(N)) hi rahega.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # using sliding window technique

        uniqueString = set()
        left = 0
        maxSize = 0
        for i in range(0,len(s)):
            while s[i] in uniqueString:
                uniqueString.remove(s[left])
                left += 1
            uniqueString.add(s[i])
            maxSize = max(maxSize,i - left + 1)

        
        print(uniqueString)
        
        return maxSize

s = "abcabcbb"
sol = Solution()

print(sol.lengthOfLongestSubstring(s))


        