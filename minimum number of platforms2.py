# 12:37

class minimumNumberOfPlatforms():
    def plateform(arr, dep):
        mergeArrival = []
        plateformCount = 0
        maxPlateform = 0
        

        for time in range(0, len(arr)):
            mergeArrival.append((arr[time],"A"))
            mergeArrival.append((dep[time],"D"))
        

        mergeArrival.sort(key = lambda x : x[0])

        for item in mergeArrival:
            if item[1] == "A":
                plateformCount += 1
                maxPlateform = max(maxPlateform, plateformCount)
            else:
                plateformCount -= 1
        

        return maxPlateform
        


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

sol = minimumNumberOfPlatforms()
print(minimumNumberOfPlatforms.plateform(arr, dep))