# Total Time Complexity = O(m log m + n log m + n²)
# Symbol	Meaning
# m	Number of products in the list → len(products)
# n	Length of the searchWord → len(searchWord)

import bisect

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort() #0(m log m)
        res = []
        prefix = ''
        
        print(products)

        for ch in searchWord: # 0(m)
            prefix += ch
            i = bisect.bisect_left(products, prefix) # use binary search 0(log n)
            suggestions = []
            
            print(i)
            

            # Check next 3 products from index i
            for j in range(i, min(i + 3, len(products))): #0(3)n
                if products[j].startswith(prefix):  # 0(n)
                    suggestions.append(products[j])
            res.append(suggestions)
        
        return res

        # arr = [10, 20, 30, 40]
        # idx = bisect.bisect_right(arr, 25)
        # print(idx)  


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

sol = Solution()

print(sol.suggestedProducts(products,searchWord))

