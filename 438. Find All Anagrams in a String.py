from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        result = []

        if len(p) > len(s):
            return result
        
        n = len(s)
        m = len(p)
        
        p_count = Counter(p)
        window_Counter = Counter(s[:m])


        if p_count == window_Counter:
            result.append(0)
        
        left = 0

        for char in range(m,n):
            window_Counter[s[char]] += 1

            window_Counter[s[left]] -= 1

            if window_Counter[s[left]] == 0:
                del window_Counter[s[left]]
            
            left += 1
            
            if window_Counter == p_count:
                result.append(left)
            
          
        
        return result


        


        



        


s = "cbaebabacd"
p = "abc"

sol = Solution()

print(sol.findAnagrams(s,p))