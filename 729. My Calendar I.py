class MyCalendar(object):

    def __init__(self):
        self.booking = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        for s,e in self.booking:
            if max(s,startTime) < min(e,endTime):
                return False
                
        self.booking.append((startTime,endTime))
        return True
        


sol = MyCalendar()
o1 = 10
o2 = 20
o3 = 20
o4 = 30
print(sol.book(o1,o2))
print(sol.book(o3,o4))

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)