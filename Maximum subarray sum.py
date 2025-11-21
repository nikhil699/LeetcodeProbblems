# using sliding window

class Solution:
    def maxSubbarray(self,nums,sum):
        maxLength = 0
        count = 0
        left = 0

        for right in range(len(nums)):
            count += nums[right]

            while count > sum:
                count -= nums[left]

                left += 1

            if count == sum:
                return [left , right]
                


        return None


arr01 = [2, 0, 0, 0, 2, 6, 4] #(0,4)
sum01 = 4

arr02 = [30, 6, 11, 3, 0, 10, 5] #(1,3)
sum02 = 20

arr03 = [5, 5, 5, 5] #(0,3)
sum03 = 20

arr04 = [7, 3, 9, 20, 1] #(3,3)
sum04 = 20

arr05 = [4, 2, 6, 2, 4, 6] #(1,3)
sum05 = 8

sol = Solution()
print(sol.maxSubbarray(arr01,sum01))
print(sol.maxSubbarray(arr02,sum02))
print(sol.maxSubbarray(arr03,sum03))
print(sol.maxSubbarray(arr04,sum04))
print(sol.maxSubbarray(arr05,sum05))