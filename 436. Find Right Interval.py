# Step 01 - understand the problem
# Problem Understanding : having an array intervals with start end where start is unique 
# [[3,4],[2,4],[1,2]]
# (3,4) , (2,3) = 3 >= 3
# hame aise interval find karne ho jo current ke end time se ya to bade ho ya to barabar ho
# Tumhe actually chahiye:
# start
# original index (because answer index maangta hai
# Time Complexity : 0(nlogn)
# Space Complexity : 0(n)


class Solution(object):
    def findRightInterval(self, intervals):

        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        heap = []
        
        for item in range(0,len(intervals)): # 0(n)
            heap.append((intervals[item][0],item))
        
        result = [-1] * len(intervals)

        heap.sort() # 0(nlogn)
        
        for item in range(0,len(intervals)): # n * log n
            unit = intervals[item][1]
            
            left, right = 0, len(heap) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2
                if heap[mid][0] >= unit:
                    ans = heap[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
            
            result[item] = ans
        

        return result
        


intervals = [[3,4],[2,3],[1,2]]

sol = Solution()

print(sol.findRightInterval(intervals))





