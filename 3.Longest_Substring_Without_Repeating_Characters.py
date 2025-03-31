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
        count = {}
        left = 0
        maxSubstringLength = 0

        for right in range(0,len(s)):
            char = s[right]
            count[char] = count.get(char,0)+1

            while count[char] > 1:
                count[s[left]] -= 1
                left += 1

            maxSubstringLength = max(maxSubstringLength, right - left +1)
        
        return maxSubstringLength


s = "abcabcbb"
sol = Solution()

print(sol.lengthOfLongestSubstring(s))


        