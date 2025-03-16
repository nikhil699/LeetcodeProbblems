class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        resultWindow = float('inf')
        result = 0
        left = 0
        right = len(nums) - 1
        nums.sort()
        


        for item in range(0,len(nums)-2):
            left = item + 1
            right = len(nums) - 1 
            while left < right:
                
                result = nums[item] + nums[left] + nums[right]
                if result == target:
                    return result
            
                if abs(target - result) < abs(target - resultWindow):
                    resultWindow = result

                if result < target:
                    left = left + 1
                else:
                    right = right - 1
                
        
    
      
        return resultWindow

sol = Solution()
nums = [-1,2,1,-4]
target = 1

print(sol.threeSumClosest(nums,target))