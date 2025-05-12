# Intutuion
# ----------
# Know the last occurrence of each character.
# Traverse the string and keep track of the furthest point (max of last indices seen so far).
# If the current index equals the end, we can partition.


# Time Complexity : 0(n)
#Space complexity : 0(1) max of 26 characters we will store
# where n is the number of character in the given input string.

class Solution(object):
    def partitionLabels(self, s):
        last = {ch: i for i, ch in enumerate(s)}
        res = []
        start = end = 0


        for i, ch in enumerate(s):
            end = max(end, last[ch])
            

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res


sol = Solution()

s = "ababcbacadefegdehijhklij"
print(sol.partitionLabels(s))