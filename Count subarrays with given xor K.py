class Solution:
    def subarraySumXOR(self,nums,k):
        prefixSum = {0:1}
        prefix = 0
        count = 0

        for item in range(0,len(nums)):
            prefix ^= nums[item]

            if prefix^k in prefixSum:
                count += prefixSum[prefix^k]
            
            prefixSum[prefix^k] = prefixSum.get(prefix^k, 0) + 1
        
        return count
                





nums = [4, 2, 2, 6, 4]
k = 6

sol = Solution()
print(sol.subarraySumXOR(nums, k))