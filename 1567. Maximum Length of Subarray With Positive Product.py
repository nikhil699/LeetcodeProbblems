class Solution(object):
    def getMaxLen(self, nums):
        pos_len = 0  # length of subarray ending here with positive product
        neg_len = 0  # length of subarray ending here with negative product
        max_len = 0

        for num in nums:
            if num == 0:
                pos_len = 0
                neg_len = 0
            elif num > 0:
                pos_len += 1
                neg_len = neg_len + 1 if neg_len > 0 else 0
            else:  # num < 0
                temp = pos_len
                pos_len = neg_len + 1 if neg_len > 0 else 0
                neg_len = temp + 1
            max_len = max(max_len, pos_len)

        return max_len


nums = [-1,-2,-3,0,1]

sol = Solution()

print(sol.getMaxLen(nums))