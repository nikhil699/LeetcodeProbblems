# Hum prefix sum le rahe hain, aur check kar rahe hain:
# agar do prefix sums ka remainder (mod k) same ho →
# toh unke beech ka subarray divisible by k hai.


class Solution(object):
    def subarraysDivByK(self, nums, k):
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        remainder_count = {0:1}
        prefixSum = 0
        count = 0
        remainder = 0

        for item in range(len(nums)):
            prefixSum += nums[item]

            remainder = prefixSum % k

            if remainder < 0:
                remainder += k
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            remainder_count[remainder] = remainder_count.get(remainder,0) + 1

        return count



nums = [4,5,0,-2,-3,1]
k = 5
sol = Solution()

print(sol.subarraysDivByK(nums,k))