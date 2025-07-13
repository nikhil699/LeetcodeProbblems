class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        result_str = num_str.replace('6', '9' , 1)

        return int(result_str)


         

sol = Solution()
nums = 6990

print(sol.maximum69Number(nums))