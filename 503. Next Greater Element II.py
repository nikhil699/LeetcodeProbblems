class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            curr = nums[i % n]
            while stack and nums[stack[-1]] < curr:
                prev_index = stack.pop()
                res[prev_index] = curr
            # Only push indices from the first traversal to avoid duplication.
            # ismein keval nums ke original length ke value daal raha hu aur koi bada mil jaye to hata raha hu
            if i < n:
                stack.append(i)
        return res
nums = [1,2,3,4,3]

sol = Solution()

print(sol.nextGreaterElements(nums))

