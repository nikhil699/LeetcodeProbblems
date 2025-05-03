class Solution(object):
    def getModifiedArray(self, length, updates):

        res = [0] * length

        for start, end, inc in updates:
            res[start] += inc
            if end + 1 < length:
                res[end + 1] -= inc

        for i in range(1,length):
            res[i] = res[i] + res[i - 1]
        
        return res


sol = Solution()

length = 5
updates = [
    [1, 3, 2],
    [2, 4, 3],
    [0, 2, -2]
]


print(sol.getModifiedArray(length, updates))