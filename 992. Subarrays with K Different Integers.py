# ismien hamk = 2 hai subArray(k) to ismain  2 tak ke sare subaaray hai agar hame sirf k(2) subaaray chaye to 
# ismein se hame subArray(k - 1) hata denge = 2 - 1 to i tak ke sare subaaray hat jayenge

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            left = 0
            maxResult = 0
            freq = {}

            for right in range(0,len(nums)):
                freq[nums[right]] = freq.get(nums[right], 0) + 1

                while len(freq) > k:
                    freq[nums[left]] -= 1
            

                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    
                    left += 1

                # subarray till k
                maxResult += right - left + 1
            
            return maxResult

        return atMost(k) - atMost(k - 1)


nums = [1,2,1,3,4]
k = 3

sol = Solution()

print(sol.subarraysWithKDistinct(nums,k))