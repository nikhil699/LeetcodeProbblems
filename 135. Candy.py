class Solution(object):
    def candy(self, ratings):

        """
        :type ratings: List[int]
        :rtype: int
        """

        leftArray = [1] * len(ratings)
        rightArray = [1] * len(ratings)
        result = []

        for item in range(1, len(ratings)):
            if ratings[item] > ratings[item - 1]:
                leftArray[item] = leftArray[item - 1] + 1
        

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                rightArray[i] = rightArray[i + 1] + 1
            

        for item in range(0, len(ratings)):
            result.append(max(leftArray[item], rightArray[item]))
        

        return sum(result)



sol = Solution()
ratings = [1,0,2]

print(sol.candy(ratings))