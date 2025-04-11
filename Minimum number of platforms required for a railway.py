def countPlatforms(n, arr, dep):
    mergedArray = []

    for item in range(0,len(arr)):
        mergedArray.append((arr[item],"A"))
        mergedArray.append((dep[item],"D"))

    mergedArray.sort()
    requiredPlateform = 0
    result = 0

    for item in mergedArray:
        if item[1] == "A":
            requiredPlateform += 1
            result = max(result,requiredPlateform)
        else:
            requiredPlateform -= 1
    
    return result



arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
n = 6

print(countPlatforms(n,arr,dep))