class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater = {}

        # Step 1: Go through nums2 and build the next_greater map
        for num in nums2: # (1:3,3:4)
            # If current number is greater than stack top, it's the next greater
            while stack and num > stack[-1]:
                prev_num = stack.pop()
                next_greater[prev_num] = num
            stack.append(num)
        

        # Step 2: For remaining elements in stack, there is no next greater
        for num in stack: # (1:3,3:4,2:-1,4:-1)
            next_greater[num] = -1

        # Step 3: Prepare result for nums1 using the map
        for index,item in enumerate(nums1):
            input01 = next_greater[item]
            nums1[index] = input01
        
        return nums1

nums1 = [4,1,2]
nums2 = [1,3,4,2]

sol = Solution()

print(sol.nextGreaterElement(nums1,nums2))

