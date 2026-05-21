class Solution(object):
    def dayOfYear(self, date):

        """
        :type date: str
        :rtype: int
        """

        monthDays = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
        }


        year, month, date = date.split("-")

        year = int(year)
        month = int(month)
        date = int(date)

        totalDays = 0

        for item in range(1, month):
            totalDays += monthDays[item]
        

        totalDays += date

        leapYear = (
            year % 400 == 0 or (year % 4 ==0 and year % 100 != 0)
        )
        

        if leapYear and month > 2:
            return totalDays + 1
        else:
            return totalDays




sol = Solution()
date = "2019-01-09"
print(sol.dayOfYear(date))