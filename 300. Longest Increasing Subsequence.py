# ⏱️ Time Complexity:
# Outer loop: O(n) (each of the n elements in nums)

# Inside: bisect_left is O(log k), where k is the length of sub (max n in worst case)

# So: Total Time = O(n log n)
# if i == len(sub):
#     sub.append(num)     # num bada hai sabse → naya increasing subsequence
# else:
#     sub[i] = num        # num chhota hai → replace karo to optimize subsequence

# sub = [2, 3]
# num = 7

# i = bisect_left(sub, 7)  # i = 2
# len(sub) = 2

# So, i == len(sub) → means 7 > sab elements in sub
# → append(7)
# → sub = [2, 3, 7]

# Time: O(n log n) — for binary search inside loop
# Space Complexity : 0 (n)


# class Solution(object):
#     def lengthOfLIS(self, nums):
#         if not nums:
#             return 0

#         n = len(nums)
#         dp = [1] * n

#         for i in range(n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)

import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        sub = []

        for num in nums:
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
                
            else:
                sub[i] = num


        return len(sub)


sol = Solution()
nums = [10,9,2,5,3,7,101,18]


print(sol.lengthOfLIS)