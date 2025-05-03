# Intuition / Approach (Min Heap Method - O(k log n))
# Since the matrix is sorted row-wise and column-wise, the smallest element is at (0,0), and its neighbors (0,1) and (1,0) are the next smallest.

# We use a min heap to always get the next smallest element.

# Initially, push (matrix[0][0], 0, 0) in the heap.

# Then, pop k elements from the heap — on each pop, push the next element from the same column (downward) if not already visited.

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        n = len(matrix)

        for i in range(min(k,n)):
            heapq.heappush(heap,(matrix[i][0],i,0)) 
        
        while k > 0:
            element,r,c = heapq.heappop(heap)

            if c + 1 < n:
                heapq.heappush(heap,(matrix[r][c + 1], r, c + 1,))
            
            k -= 1
        
        return element

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

sol = Solution()

print(sol.kthSmallest(matrix,k))