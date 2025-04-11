# Aapka result list mutable objects store karta hai, aur ismein direct reference store hota hai, na ke naye objects.
# Matlab jab aap previous_interval[1] = max(previous_interval[1], current_interval[1]) update karte ho, toh result 
# ke andar bhi same interval modify ho jata hai.
# Time Complexity : 0(n log n)
# Space Complexity : 0(n) where n is the number of elelment in a intervals

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        result = []
     

        intervals.sort()
        result.append((intervals[0]))
        print(intervals)
        for item in range(1,len(intervals)):
            current_interval = intervals[item]  
            previous_interval = result[-1]  

            if previous_interval[1] >= current_interval[0]:
                previous_interval[1] = max(previous_interval[1] , current_interval[1])
            
            else:
                result.append((current_interval))
            
            
        return result
    


intervals = [[1,3],[2,6],[8,10],[15,18]]
sol = Solution()

print(sol.merge(intervals))

