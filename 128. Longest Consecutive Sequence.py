class Solution(object):
    def longestConsecutive(self, nums):
        
        if not nums:
            return 0

        longest, s = 0, set(nums)

        for num in nums:
            cur_longest, j = 1, 1
            while num - j in s: 
                s.remove(num - j)
                cur_longest = cur_longest + 1
                j += 1

            j = 1

            while num + j in s: 
                s.remove(num + j)
                cur_longest = cur_longest + 1
                j += 1
                
            longest = max(longest, cur_longest)
        return longest


        


nums = [9, 1, 4, 7, 3, -1, 0, 5, 100, 102, 8, -1, 6]
sol = Solution()
print(sol.longestConsecutive(nums))


 # nums.sort() # n log n , nums = [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9, 100, 102]

        # longest = 1
        # current = 1

        # for right in range(1, len(nums)):
        #     if nums[right] == nums[right - 1]:
        #         continue  # skip duplicate

        #     elif nums[right] == nums[right - 1] + 1:
        #         current += 1
        #         longest = max(longest, current)
            
        #     else:
        #         current = 1

        # return longest
