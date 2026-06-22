class Solution(object):
    def rotatedDigits(self, n):

        """
        :type n: int
        :rtype: int
        """

        count = 0

        for item in range(1, n + 1):
            i = item
            isValid = True
            hasChanges = False

            while i > 0:

                element = i % 10

                if element in {3,4,7}:
                    isValid = False
                    break
                
                if element in {2,5,6,9}:
                    hasChanges = True

                i = i // 10
            
            
            if isValid and hasChanges:
                count += 1

        

        return count

sol = Solution()
n = 10
print(sol.rotatedDigits(n))