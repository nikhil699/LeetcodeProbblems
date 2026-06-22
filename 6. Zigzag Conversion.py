class Solution(object):
    def convert(self, s, numRows):

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or len(s) <= numRows:
            return s
        
        rows = [""] * numRows
        currRow = 0
        goingDown = False

        for ch in s:
            rows[currRow] += ch

            if currRow == 0 or currRow == numRows - 1:
                goingDown = not goingDown
            
            if goingDown:
                currRow += 1
            else:
                currRow -= 1

        return "".join(rows)


sol = Solution()
s = "PAYPALISHIRING"
numRows = 3

print(sol.convert(s, numRows))