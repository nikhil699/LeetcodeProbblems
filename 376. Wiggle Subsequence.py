# Correct Intuition kya honi chahiye?
# Har step par decide karo:
# Kya current element previous se bada hai (to up trend mila), ya chhota hai (to down trend mila)?
# Jab bhi direction change ho:
# Up ke baad down ya Down ke baad up → tabhi valid wiggle milega.
# Isliye hume up aur down variables rakhne padte hain jo properly track karein ki pehle kya trend tha aur ab kya hai.


class Solution(object):
    def wiggleMaxLength(self, nums):
        if not nums:
            return 0

        up = down = 1  # up: longest ending with an up, down: longest ending with a down

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1

        return max(up, down)
        

nums = [1,7,4,9,2,5]
sol = Solution()
print(sol.wiggleMaxLength(nums))