class Solution(object):
    def meetingsRooms(self, meetings):

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        meetings.sort()

        for item in range(1,len(meetings)):
            prevMeeting = meetings[item - 1]
            currMeeting = meetings[item]

            if prevMeeting[1] > currMeeting[0]:
                return False
        

        return True




meetings = [[0,30],[5,10],[15,20]]

sol =  Solution()
print(sol.meetingsRooms(meetings))