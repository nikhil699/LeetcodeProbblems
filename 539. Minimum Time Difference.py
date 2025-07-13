class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        
        # Convert "HH:MM" → minutes
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(":"))
            total = h * 60 + m
            minutes.append(total)

        minutes.sort() # [0, 1439]

        # Initialize min_diff with max possible
        min_diff = float('inf')

        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)
        
        # print(min_diff) # 1439

        # Check wrap-around: last and first element or the samllest and largest time
        wrap_around = 1440 + minutes[0] - minutes[-1]  # full day = 1440 mins
        min_diff = min(min_diff, wrap_around)

        return min_diff

        
timePoints = ["00:00","23:59","00:00"]
sol = Solution()

print(sol.findMinDifference(timePoints))