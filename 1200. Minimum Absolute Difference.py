class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = float('inf')
        result = []

        for item in range(1,len(arr)):
            diff = arr[item] - arr[item - 1]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[item - 1],arr[item]]] # reset the array if I found any mininum(min_diff) than diff.
            
            elif diff == min_diff:
                result.append([arr[item - 1],arr[item]])
        
        return result

arr = [3,8,-10,23,19,-4,-14,27]
sol = Solution()
print(sol.minimumAbsDifference(arr))