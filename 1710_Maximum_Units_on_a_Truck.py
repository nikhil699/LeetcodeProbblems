class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: -x[1])
        total_units = 0

        for item, size in boxTypes:
            if truckSize <= 0:
                return total_units
            
            boxes_to_take = min(truckSize,item)
            total_units += boxes_to_take * size 
            truckSize -= boxes_to_take
        
        
        return total_units

sol = Solution()
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

print(sol.maximumUnits(boxTypes, truckSize))