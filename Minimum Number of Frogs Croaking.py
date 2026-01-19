class Solution:
    def meetingRoomTwo(self, meetings):
        meetings.sort()

        result = [meetings[0]]


        for item in range(1,len(meetings)):
            prevMeetings = result[-1] 
            currMeetings = meetings[item]

            if prevMeetings[1] > currMeetings[0]:
                prevMeetings[1] = max(prevMeetings[1], currMeetings[1])
            else:
                result.append(currMeetings)
        print(result)
                
        
        return len(result)
    





meetings = [[0, 30], [5, 10], [15, 20]]

sol = Solution()

print(sol.meetingRoomTwo(meetings))