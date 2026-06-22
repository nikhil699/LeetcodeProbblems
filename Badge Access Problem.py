class Solution(object):
    def badge_Access_Problem(self, badge_records):

        entered_without_exiting = set()
        exited_without_entering = set()
        inside = set()

        for employee, activity in badge_records:

            if activity == "enter":

                if employee in inside:
                    entered_without_exiting.add(employee)
                else:
                    inside.add(employee)
            
            else:

                if employee not in inside:
                    exited_without_entering.add(employee)
                else:
                    inside.remove(employee)
        

        entered_without_exiting.update(inside)


        return {
            "entered_without_exiting" : list(entered_without_exiting),
            "exited_without_entering" : list(exited_without_entering)
        }


sol = Solution()

badge_records = [
    ["Martha", "exit"],
    ["Paul", "enter"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "enter"],
    ["Paul", "enter"],
    ["Curtis", "exit"],
    ["Paul", "exit"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "exit"]
]

print(sol.badge_Access_Problem(badge_records))