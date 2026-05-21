class Solution(object):
    def intervalIntersection(self, firstList, secondList):

        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """

        
        i = 0
        j = 0
        result = []

        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                result.append((start,end))
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result
    
sol = Solution()

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

print(sol.intervalIntersection(firstList, secondList))