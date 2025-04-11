# Given two arrays, arr[] and dep[], that represent the arrival and departure 
#times of trains respectively, the task is to find the minimum number of platforms required so that no train waits.

# arr[] = [900, 940, 950, 1100, 1500, 1800]
# dep[] =  [910, 1200, 1000, 1130, 1900, 2000]
# Output: 3 
#Explanation: There are at-most three trains at a time (time between 940 to 1200)



def countStation(arr,dep):

    sizeOfArrival = len(arr)
    mergedArray = []

    for i in range(0,sizeOfArrival):
        mergedArray.append((arr[i],"A"))
        mergedArray.append((dep[i],"D"))

    countStation = 1
    mergedArray.sort()
    result = 1

    for i in range(0,len(mergedArray)):
        item = mergedArray[i]
        if item[1] == "A":
            countStation = countStation + 1

            result = max(result,countStation)
        else:
            countStation = countStation - 1

    
    print(result)


arr = [900, 940, 950, 1100, 1500, 1800]
dep =  [910, 1200, 1000, 1130, 1900, 2000]

countStation(arr,dep)