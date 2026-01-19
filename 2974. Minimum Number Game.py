class Solution:
    def numberGame(self, nums):
        nums.sort()
        result = []

        for item in range(0, len(nums), 2):
            result.append(nums[item + 1])
            result.append(nums[item])

        return result


sol = Solution()

nums = [5,4,2,3]

print(sol.numberGame(nums))