class solution:
    def meetingRoomOne(self, meetings):
        meetings.sort()


        for item in range(1,len(meetings)):
            prevMeetings = meetings[item - 1] 
            currMeetings = meetings[item]

            if prevMeetings[1] > currMeetings[0]:
                return False
        
        return True
    





meetings = [[0, 30], [5, 10], [15, 20]]

sol = solution()

print(sol.meetingRoomOne(meetings))