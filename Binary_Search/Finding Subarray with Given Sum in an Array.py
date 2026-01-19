# Using Two Pointers + Sliding Window
class Solution(object):
    def subarrayWithGivenSumInAnArray(self, nums, target):

        currSum = 0
        left = 0

        for item in range(0, len(nums)):
            currSum += nums[item]
            
            while currSum > target:
                currSum -= nums[left]

                left += 1
            
            if currSum == target:
                return (left,item)
        

        return -1
    # intution
    # Har index tak ka cumulative sum rakho.
    # Agar Prefix Sum - target pehle aa chuka hai, to beech ka subarray target ke barabar hai.   
    # Using Prefix Sum + Hashmap
    def subarrayWithGivenSumInAnArrayWithNegetiveNumber(self, nums, target):

        prefixSum = 0
        sumIndexMap = {0 : -1}

        for item in range(0, len(nums)):
            prefixSum += nums[item]

            if (prefixSum - target) in sumIndexMap:
                return (sumIndexMap[(prefixSum - target)] + 1, item)

            if prefixSum not in sumIndexMap:
                sumIndexMap[prefixSum] = item
        
        return -1

        


nums = [36, 6, 11, 3, 0, 10, 5]  # Output : 1 to 3 
target = 20
nums02 = [10, 2, -2, -20, 10] # Output : 0 to 3
target02 = -10
sol = Solution()

print(sol.subarrayWithGivenSumInAnArray(nums, target))
print(sol.subarrayWithGivenSumInAnArrayWithNegetiveNumber(nums02,target02))






