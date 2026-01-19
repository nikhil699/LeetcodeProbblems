class Solution:
    def trainPlateform(self, arr, dep):

        countPlateform = []
        

        for right in range(0,len(arr)):
            countPlateform.append((arr[right], "A"))
            countPlateform.append((dep[right], "D"))
        
        overallPlateform = 0
        maxPlateform = 0

        countPlateform.sort()

        for item in countPlateform:
            if item[1] == "A":
                overallPlateform += 1
                maxPlateform = max(maxPlateform, overallPlateform)
            
            else:
                overallPlateform -= 1

        return maxPlateform



arr = [900, 940, 950, 1100, 1500, 1800]   # [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000] # [910, 1120, 1130, 1200, 1900, 2000]

sol = Solution()

print(sol.trainPlateform(arr, dep))

