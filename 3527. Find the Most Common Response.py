import heapq
class Solution(object):
    def findCommonResponse(self, responses):

        """
        :type responses: List[List[str]]
        :rtype: str
        """

        countFrequency = {}

        for item in responses:
            currItem = set(item)
            for element in currItem:
                if element not in countFrequency:
                    countFrequency[element] = 1
                else:
                    countFrequency[element] += 1

        heap = []
        
        for item in countFrequency:
            heapq.heappush(heap, (-countFrequency.get(item), item))
        
        result = heapq.heappop(heap)[1]

        return result
        

            
sol = Solution()

responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]

print(sol.findCommonResponse(responses))