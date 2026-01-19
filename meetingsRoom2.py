class Solution():
    def meetingRoomTwo(self, meetings):
        overallMetings = []

        for item in meetings:
            overallMetings.append((item[0],"A"))
            overallMetings.append((item[1],"D"))
        
        roomsRequired = 0
        maxRoomsRequired = 0

        overallMetings.sort()

        for item in overallMetings:
            if item[1] == "A":
                roomsRequired += 1
                maxRoomsRequired = max(maxRoomsRequired, roomsRequired)
            else:
                roomsRequired -= 1
        
        return maxRoomsRequired
    
    

Input = [[0, 30], [5, 10], [15, 20]]
sol = Solution()

print(sol.meetingRoomTwo(Input))