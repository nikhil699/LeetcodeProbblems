import heapq
class Solution(object):
    def findRestaurant(self, list1, list2):

        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        # heap = []

        # for item in range(0 , len(list1)):
        #     if list1[item] in list2:
        #         heapq.heappush(heap, (list1[item], item))
        
        # resultItem = heapq.heappop(heap)[0]

        # return [resultItem]

        index_map = {}
        minIndex = float('inf')
        result = []

        for index, item in enumerate(list1): # 0(n)
            index_map[item] = index
        

        for index, item in enumerate(list2): # 0(n)
            if item in index_map: # 0(1)
                indexSum = index + index_map[item]

                if indexSum < minIndex:
                    minIndex = indexSum
                    result = [item]
                
                elif indexSum == minIndex:
                    result.append(item)

        return result


sol = Solution()
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(sol.findRestaurant(list1, list2))