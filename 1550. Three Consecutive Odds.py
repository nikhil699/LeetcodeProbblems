# using Two pointer approach
class Solution(object):
    def threeConsecutiveOdds(self, arr):

        """
        :type arr: List[int]
        :rtype: bool
        """

        count = 0
        maxCount = 0

        for right in range(0, len(arr)):
            if arr[right] % 2 != 0:
                count += 1
            else:
                count = 0
            maxCount = max(maxCount, count)

        
        if maxCount >= 3:
            return True
        else:
            return False
            
             

sol = Solution()

arr = [1,2,34,3,4,5,7,23,12]

print(sol.threeConsecutiveOdds(arr))