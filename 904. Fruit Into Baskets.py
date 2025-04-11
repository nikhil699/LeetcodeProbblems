class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket = {}
        maxCount = 0
        left = 0

        for fruit in range(0,len(fruits)):
            basket[fruits[fruit]] = basket.get(fruits[fruit],0)+1

            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            maxCount = max(maxCount, fruit - left + 1)

        return maxCount 

fruits = [1,1,2,2,1,2,3,4]

sol = Solution()

print(sol.totalFruit(fruits))